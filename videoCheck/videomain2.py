"""video main
기능설명:
     비디오로 근무시간을 측정하는 기능
개발자:
    송재임, 유현지
개발일시:
    2021.01.17.13.17.00
버전:
    0.0.3
"""
import io
from datetime import datetime, timedelta

from PIL import Image
import face_recognition
import cv2
import numpy as np
import logging

from info.loginfo import LogInfo
from info.settingInfo import SettingInfo
from info.userinfo import UserInfo
from info.workinfo import ArrayWorkInfo


class FaceRecog:
    _instance = None

    @classmethod
    def _getInstance(cls):
        print("[video.py] _getInstance call")
        cls._instance.reset()
        return cls._instance

    @classmethod
    def instance(cls, *args, **kargs):
        print("[video.py] instance call")
        cls._instance = cls(*args, **kargs)
        cls.instance = cls._getInstance
        return cls._instance

    def __init__(self):
        print("[video.py] __init__ call")
        settingInfo = SettingInfo.instance()
        self.RECOG_LV = settingInfo.RECOV_LV
        self.NOD_SEC = settingInfo.NOD_SEC
        self.VID_INTVL = settingInfo.VID_INTVL

        self.logInfo = LogInfo.instance()

        self.route = None

        self.userInfo = UserInfo.instance()
        self.name = self.userInfo.name
        self.image = self.userInfo.image

        self.logger = None

        self.known_face_encodings = []
        self.known_face_names = []
        self.set_image_to_known()

    def reset(self):
        print("reset 호출")

        print("Setting is applied to VIDEO object!")
        print("NOD_SEC : " + str(self.NOD_SEC))
        print("VID_INTVL : " + str(self.VID_INTVL))
        print("RECOV_LV : " + str(self.RECOG_LV))

        self.working = False
        # 화면에 잡힌 얼굴중 근무자가 존재하는지를 알아내는 boolean 변수
        self.workerExist = False
        self.paused = False

        self.face_locations = []
        self.face_encodings = []
        self.face_names = []
        self.process_this_frame = True
        self.video_end = False

        self.index = -1
        self.first = True
        self.totalFrame = 0
        self.recogFrameAgg = 0
        self.recogFrame = 0
        self.notRecogFrame = 0
        self.notRecogAgg = 0

        self.notRecogStartPoint = 0
        self.notRecogEndPoint = 0

        self.alertSlackOff = False
        self.work_info = {}
        self.work_info['date_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.work_info['work_type'] = "video"
        self.work_info_array = ArrayWorkInfo.instance().work_info_array

        self.logger = self.get_logger()
        self.logger.info("동영상 근무측정 시작")

    def get_logger(self):
        # logger instance 생성
        logger = logging.getLogger(__name__)

        # handler 생성 (stream, file)
        if len(logger.handlers) > 0:
            return logger

        # FORMAT = '[%(asctime)s] %(levelname)s - %(name)s - %(message)s'
        FORMAT = '[%(asctime)s]- %(message)s'
        TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
        formatter = logging.Formatter(FORMAT, TIME_FORMAT)

        streamHandler = logging.StreamHandler()
        streamHandler.setFormatter(formatter)

        fileHandler = logging.FileHandler(self.logInfo.file_path, encoding="utf-8")
        fileHandler.setFormatter(formatter)
        # logger instance에 handler 설정
        logger.addHandler(streamHandler)
        logger.addHandler(fileHandler)
        # logger instance로 log 찍기
        logger.setLevel(level=logging.DEBUG)

        return logger

    # 비디오 경로 설정
    def set_file_route(self, route):
        self.route = route
        self.logger.info(self.route)
        self.get_video_info()

    # 비디오 정보 가져오기
    def get_video_info(self):
        self.video = cv2.VideoCapture(self.route)
        self.FPS = round(self.video.get(cv2.CAP_PROP_FPS), 2)

        # fps 값이 없다면 기본값인 30으로 설정
        if self.FPS == 0:
            self.FPS = 30

        self.time_length = round(self.video.get(cv2.CAP_PROP_FRAME_COUNT) / self.FPS)
        print("비디오 총길이 : " + str(self.time_length) + "초")

        # 몇 frame 간격으로 넘어갈 것인지 설정
        self.interval = round(self.FPS) * self.VID_INTVL
        self.totalFrame = -self.interval
        self.frame_sequence = -self.interval
        self.specific_frame = []

    # 사용자 이미지 설정
    def set_image_to_known(self):
        self.known_face_names.append(self.name)
        mode = 'RGB'
        im = Image.open(io.BytesIO(self.image))
        if mode:
            im = im.convert(mode)
        img = np.array(im)

        face_encoding = face_recognition.face_encodings(img)[0]
        self.known_face_encodings.append(face_encoding)

    # 근무여부를 확인하는 boolean 변수를 반환한다.
    @property
    def working(self):
        return self._working

    @working.setter
    def working(self, value):
        self._working = value

    def get_name(self, name):
        self.name = name
        print(self.name)

    def get_video(self):
        return self.video

    def set_frame_list(self, frame_list):
        self.specific_frame = frame_list

    def get_specific_frame(self):
        percent = 0
        self.frame_sequence += self.interval

        if self.time_length != 0 and self.FPS != 0:
            if self.frame_sequence > self.time_length * self.FPS:
                return None, 100
            if self.frame_sequence != 0:
                percent = int((self.frame_sequence / (self.FPS * self.time_length)) * 100)
                # print(str(percent) + "% 진행중")
        else:
            percent = -1

        self.video.set(cv2.CAP_PROP_POS_FRAMES, self.frame_sequence)
        ret, frame = self.video.read()
        if frame is not None:
            # print("프레임 가져오기 성공")
            return frame, percent
        else:
            print("끝!")
            return None, percent

    def do_recognition(self):
        self.index += 1
        if self.index >= len(self.specific_frame):
            print("index : " + str(self.index) + ", frame_length : " + str(len(self.specific_frame)))
            return None

        self.totalFrame += self.interval
        frame = self.specific_frame[self.index]
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]
        # 계산 양을 더 줄이기 위해서 두 frame당 1번씩만 계산합니다.
        # Only process every other frame of video to save time
        if self.process_this_frame:
            self.face_locations = face_recognition.face_locations(rgb_small_frame)
            self.face_encodings = face_recognition.face_encodings(rgb_small_frame, self.face_locations)
            self.face_names = []

            for face_encoding in self.face_encodings:
                if self.RECOG_LV == 1:
                    name = self.name
                elif self.RECOG_LV >= 2:
                    distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
                    min_value = min(distances)

                    # tolerance: How much distance between faces to consider it a match. Lower is more strict.
                    # 0.6 is typical best performance.
                    # 실험상, 거리가 0.6 이면 다른 사람의 얼굴입니다. 이런 경우의 이름은 Unknown 입니다.

                    # 거리가 0.6 이하이고, 최소값을 가진 사람의 이름을 찾습니다.
                    name = "Unknown"
                    if min_value < 0.6:
                        # 최소 값을 반환한 행렬을 찾는다.
                        index = np.argmin(distances)
                        name = self.known_face_names[index]

                self.face_names.append(name)

        self.process_this_frame = not self.process_this_frame

        if self.first is False and self.alertSlackOff is False and self.notRecogFrame >= self.NOD_SEC * self.FPS:
            recog_sec = self.recogFrame / self.FPS
            self.alertSlackOff = True
            self.logger.info('근무태만')
            self.logger.info('근무유지시간 : ' + format(recog_sec, ".1f") + "초")
            self.recogFrame = 0

        ############
        # Display the results
        # 찾은 사람의 얼굴 영역과 이름을 비디오 화면에 그립니다.
        # 프레임 안에 얼굴이 있으면
        if len(self.face_locations) != 0:
            self.workerExist = False
            for face_name in self.face_names:
                # 해당 조건문을 사용자 입력값으로 받으면 원하는 사람의 근무여부만 체크할 수 있지 않을까?
                if face_name == self.name:
                    self.workerExist = True
                    break

            if self.workerExist:
                self.recogFrame += self.interval
                self.recogFrameAgg += self.interval

            if self.workerExist and not self.working:  # 얼굴 인식이 안되다가 인식이 된 순간
                if self.notRecogFrame < self.NOD_SEC * self.FPS:  # 10초 * fps
                    self.recogFrameAgg += self.notRecogFrame
                    self.recogFrame += self.notRecogFrame
                else:
                    self.notRecogAgg += self.notRecogFrame
                    self.alertSlackOff = False

                if self.first:
                    self.logger.info('근무시작 : ' + str(timedelta(seconds=int(self.totalFrame / self.FPS))))
                    self.first = False
                else:
                    # count : 현재까지의 총근무시간(태만시간포함)
                    total_sec = self.totalFrame / self.FPS
                    not_recog_sec = self.notRecogFrame / self.FPS
                    recog_sec = self.recogFrameAgg / self.FPS
                    # not_recog_agg = self.notRecogAgg / self.FPS
                    if not_recog_sec >= self.NOD_SEC:
                        self.notRecogEndPoint = total_sec
                        strNotRecogStart = str(timedelta(seconds=int(self.notRecogStartPoint)))
                        strNotRecogEnd = str(timedelta(seconds=int(self.notRecogEndPoint)))
                        self.logger.info('태만유지시간 : ' + format(not_recog_sec, ".1f") + '초(' + strNotRecogStart + "~" + strNotRecogEnd + ")")
                        # self.logger.info('근무누적시간 : ' + format(recog_sec, ".1f") + '초/' + format(total_sec, ".1f") + '초')
                    self.notRecogFrame = 0
                self.working = True

        #프레임에 얼굴이 없거나, 근무자가 없는 경우
        if self.first is False and (len(self.face_locations) == 0 or not self.workerExist):

            if self.working:  # 얼굴인식이 되다가 안되기 시작한 첫 번째 순간
                self.notRecogFrame = self.interval
                self.notRecogStartPoint = self.totalFrame / self.FPS
            else:  # 계속 얼굴 인식이 안되는 순간
                self.notRecogFrame += self.interval
            self.working = False

        # for (top, right, bottom, left), name in zip(self.face_locations, self.face_names):
        #     # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        #     top *= 4
        #     right *= 4
        #     bottom *= 4
        #     left *= 4
        #
        #     # Draw a box around the face
        #     cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        #
        #     # Draw a label with a name below the face
        #     if self.RECOG_LV >= 2:
        #         cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        #         font = cv2.FONT_HERSHEY_DUPLEX
        #         cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        return frame

    def calculate_total(self):
        # 영상 마지막에 근무자가 인식이 되지 않는다면 태만시간에 대한 계산이 끝나지 않으므로
        # 영상이 마친 후 계산을 한번 더 해준다.
        total_sec = self.totalFrame / self.FPS
        recog_sec = self.recogFrameAgg / self.FPS
        if self.notRecogFrame != 0:
            if self.notRecogFrame < self.NOD_SEC * self.FPS:
                self.recogFrameAgg += self.notRecogFrame
                self.notRecogFrame = 0
            else:
                self.notRecogEndPoint = total_sec
                strNotRecogStart = str(timedelta(seconds=int(self.notRecogStartPoint)))
                strNotRecogEnd = str(timedelta(seconds=int(self.notRecogEndPoint)))

                self.notRecogAgg += self.notRecogFrame
                not_recog_sec = self.notRecogFrame / self.FPS
                self.notRecogEndPoint = total_sec
                self.logger.info('태만유지시간 : ' + format(not_recog_sec, ".1f") + '초(' + strNotRecogStart + "~" + strNotRecogEnd + ")")

        # 근무시간 계산
        if self.time_length != 0 and self.totalFrame / self.FPS + 1 > self.time_length:
            totalTime = self.time_length
        else:
            totalTime = int(self.totalFrame / self.FPS)

        strTotalTime = str(timedelta(seconds=totalTime))

        recogTime = int((self.recogFrameAgg / self.totalFrame) * totalTime)
        strRecogTime = str(timedelta(seconds=recogTime))

        notRecogTime = totalTime - recogTime

        # 총태만시간이 10초 미만일 수는 없다.
        if notRecogTime < self.NOD_SEC:
            recogTime += notRecogTime
            notRecogTime = 0

        strNotRecogTime = str(timedelta(seconds=notRecogTime))

        self.work_info['total_time'] = totalTime
        self.work_info['work_time'] = recogTime
        self.work_info['not_work_time'] = notRecogTime
        self.work_info_array.append(self.work_info)

        str_noti_end = "프로그램 종료"
        self.logger.info(str_noti_end)
        print("\n동영상 fps : " + str(self.FPS) + "\n" \
                               + "전체 프레임 : " + str(self.totalFrame) \
                               + "\n" + "인식된 프레임 : " + str(self.recogFrameAgg) + "\n" \
                               + "인식되지 않은 프레임 : " + str(self.notRecogAgg) + "\n")

        str_total_working_time = "총근무시간 : " + strTotalTime + "\n" \
            + "순수근무시간 : " + strRecogTime + "\n" \
            + "총태만시간 : " + strNotRecogTime + "\n"
        self.logger.info(str_total_working_time + "\n")
        return str_total_working_time

