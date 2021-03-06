"""realtime face recognition
기능설명:
    실시간으로 사용자의 얼굴을 인식하여 근태 여부를 확인한다. 얼굴인식이 10초 이상 되지않으면 근무태만으로 간주한다.
개발자:
    송재임 유현지
개발일시:
    2021.01.12.02.07.00
버전:
    0.0.5
"""
import io
import threading

import face_recognition
import cv2
import numpy as np

from datetime import datetime, timedelta

from PIL import Image, ImageDraw, ImageFont

from info.settingInfo import SettingInfo
from info.userinfo import UserInfo
import logging
import timeit

from negligencedetection.negligence_detection_2021_0209 import Detection
from realTimeCheck import camera
from info.workinfo import ArrayWorkInfo
from info.loginfo import LogInfo


class FaceRecog(object):
    _instance = None

    @classmethod
    def _getInstance(cls):
        print("_getInstance call")
        cls._instance.reset()
        return cls._instance

    @classmethod
    def instance(cls, *args, **kargs):
        print("instance call")
        cls._instance = cls(*args, **kargs)
        cls.instance = cls._getInstance
        return cls._instance

    def __init__(self):
        print("__init__ is called\n")
        self.detection = Detection()
        settingInfo = SettingInfo.instance()
        self.RECOG_LV = settingInfo.RECOV_LV
        self.NOD_SEC = settingInfo.NOD_SEC
        self.DETEC_SEC = settingInfo.DETEC_SEC

        self.work_id = 0
        self.userInfo = UserInfo.instance()
        self.known_face_encodings = []
        self.known_face_names = []
        self.video = None
        self.detection_thread = None
        self.logger = None

        self.name = self.userInfo.name
        self.image = self.userInfo.image
        self.set_image_to_known()

    def set_image_to_known(self):
        self.known_face_names.append(self.name)
        mode = 'RGB'
        im = Image.open(io.BytesIO(self.image))
        if mode:
            im = im.convert(mode)
        img = np.array(im)

        face_encoding = face_recognition.face_encodings(img)[0]
        self.known_face_encodings.append(face_encoding)

    def reset(self):
        print("variable reset")
        print("\nSetting is applied to REALTIME object!")
        print("DETEC_SEC : " + str(self.DETEC_SEC))
        print("NOD_SEC : " + str(self.NOD_SEC))
        print("RECOV_LV : " + str(self.RECOG_LV) + "\n")

        self.working = False
        # 화면에 잡힌 얼굴중 근무자가 존재하는지를 알아내는 boolean 변수
        self.workerExist = False
        self.paused = False
        # log 출력 형식

        print("카메라 가져오기 전")
        self.video = camera.VideoCamera()
        # 근무 최초 시작시간 초기화
        self.workStartTimeAtFirst = 0
        # 근무 유지 시작 시간 초기화 (근무 최초 시작시, 태만->근무중 전환시 마다 초기화 됨)
        self.workStartTime = 0
        # 근무 유지 시간 초기화 (..)
        self.workCount = 0
        # 근무 중단 시간을 담기 위한 임시 변수 초기화
        self.tempWorkStopTime = 0
        # 총 근무 시간 초기화 (계산전 : 근무 최초 시작 이래 무조건 계속 증가..근무 종료시에 - totalSlcakOffCount)
        self.totalWorkingCount = 0
        # 근무 태만 시작시간 초기화
        self.slackOffStartTime = 0
        # 근무 태만 시간 초기화 (재근무 시 마다 초기화)
        self.slackOffCount = 0
        # 근무 태만 10초 이상시 근무태만이 시작되었다는 것을 알려주었는지 체크(무한 print 방지)
        self.alertSlackOff = False
        # 근무 태만 10초 이상시 진짜 근무태만임.
        self.isRealSlackOff = False
        # 총 근무 태만 시간 초기화 (재근무 시 마다 + slackOffCount )
        self.totalSlackOffCount = 0

        self.face_locations = []
        self.face_encodings = []
        self.face_names = []
        self.process_this_frame = True
        self.video_end = False

        self.work_info = {}
        self.work_id = self.work_id + 1
        self.work_info['id'] = self.work_id
        self.work_info['date_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.work_info['work_type'] = "real"
        self.work_info_array = ArrayWorkInfo.instance().work_info_array

        # 인식 단계가 3단계라면 화면탐지코드 실행
        if self.RECOG_LV == 3:
            self.negligence_detection()

        self.logger = self.get_logger()
        self.logger.info("실시간 근무측정 시작")

    def negligence_detection(self):
        threading.Thread(target=self.detection.detect, args=(self.work_id,)).start()
        self.detection_thread = threading.Timer(self.DETEC_SEC, self.negligence_detection)
        self.detection_thread.start()

    def get_logger(self):
        # logger instance 생성
        logger = logging.getLogger(__name__)

        # handler 생성 (stream, file)
        if len(logger.handlers) > 0:
            return logger

        # format = '[%(asctime)s] %(levelname)s - %(name)s - %(message)s'
        format = '[%(asctime)s]- %(message)s'
        TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
        self.formatter = logging.Formatter(format, TIME_FORMAT)

        streamHandler = logging.StreamHandler()

        logInfo = LogInfo.instance()
        fileHandler = logging.FileHandler(logInfo.file_path, encoding="utf-8")
        # logger instance에 handler 설정
        logger.addHandler(streamHandler)
        logger.addHandler(fileHandler)
        # logger instance로 log 찍기
        logger.setLevel(level=logging.INFO)
        streamHandler.setFormatter(self.formatter)
        fileHandler.setFormatter(self.formatter)

        return logger

    @property
    def isRealSlackOff(self):
        return self._isRealSlackOff

    @isRealSlackOff.setter
    def isRealSlackOff(self, value):
        self._isRealSlackOff = value


    @property
    def working(self):
        return self._working

    @working.setter
    def working(self, value):
        self._working = value

    def __del__(self):
        print("face_recog 객체 소멸")

    def get_name(self, name):
        self.name = name
        print(self.name)

    def notifyIsPaused(self, paused):
        self.paused = paused

    def close(self):
        self.video.end_camera()
        if self.detection_thread is not None:
            self.detection_thread.cancel()

    def get_frame(self):
        frame = self.video.get_frame()

        if frame is None:
            self.video_end = True
            return None

        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]

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
                    if min_value < 0.5:
                        # 최소 값을 반환한 행렬을 찾는다.
                        index = np.argmin(distances)
                        name = self.known_face_names[index]

                self.face_names.append(name)

        self.process_this_frame = not self.process_this_frame

        # self.slackOffCount != 0 없으면 맨처음 코드를 실행했을때
        # slackOffCount = 0 이니까 무조건 10 이상임
        if self.slackOffCount != 0 and (
                timeit.default_timer() - self.slackOffCount) >= self.NOD_SEC and self.alertSlackOff is False:
            # True로 설정하면 근무 태만 알림 문구를 더이상 출력 안함
            self.alertSlackOff = True
            # self.logger.info("근무 태만 : {0}".format(self.slackOffStartTime))
            # 근무 유지 시간 계산 (근무를 한번도 안하고 바로 근무 태만될 가능성 생각 => workCount가 0일 가능성 고려)
            if self.workCount != 0:
                # count = timeit.default_timer() - self.workCount
                # count = self.tempWorkStopTime - self.workCount
                # => self.tempWorkStopTime을 사용해서 시간 계산에 마이너스 오류가 발생한 거였음..
                # 얼굴인식이 되면서 근무자가 아닌경우에는 self.tempWorkStopTime 를 초기화 안했었음..
                count = self.slackOffCount - self.workCount
                self.logger.info(f'근무 유지 시간 : ' + str(timedelta(seconds=count)).split(".")[0])
            self.logger.info(f'근무 태만 시작')
            # 진짜 근무 태만 상태임
            self.isRealSlackOff = True
        # Display the results
        # 찾은 사람의 얼굴 영역과 이름을 비디오 화면에 그립니다.
        # 프레임 안에 얼굴이 없으면(근무지 이탈) '근무 태만'
        if len(self.face_locations) == 0 and self.working is True:
            # 근무태만이 시작된 시간 저장..
            self.slackOffStartTime = datetime.now().replace(microsecond=0)
            self.slackOffCount = timeit.default_timer()
            # 아직 실제로 근무 태만은 아니다.
            self.working = False
            # 근무 중단이 된 시간을 저장 (이게 왜 필요하지? 그냥 slackOffCount 쓰면 되지않나?그리고 프레임안에 얼굴이 있되, 근무자가 아닌경우엔 self.tempWorkStopTime을 안사용하는데?)
            self.tempWorkStopTime = timeit.default_timer()
            # start_time = datetime.now().replace(microsecond=0)
            # self.logger.info("근무 태만 : {0}".format(start_time) )
        else:
            # 프레임 안에 얼굴이 있되, 근무자가 있는 경우와 없는 경우를 구분
            # 일단 프레임안에 얼굴이 존재하면, workerExist = False 초기화
            self.workerExist = False
            for face_name in self.face_names:
                # 해당 조건문을 사용자 입력값으로 받으면 원하는 사람의 근무여부만 체크할 수 있지 않을까?
                if face_name == self.name:
                    self.workerExist = True
                    break
            # 프레임 안에 근무자가 있으면 근무중
            if self.workerExist == True and self.working == False:
                # 근무중임을 갱신할 때 마다 시간을 찍는다.
                # 최초 근무 시작 시간이 저장되어 있지 않은 경우 저장
                if (self.workStartTimeAtFirst == 0):
                    self.workStartTimeAtFirst = datetime.now().replace(microsecond=0)
                    # self.logger.info("\n\n근무 시작 시간: {0}".format(self.workStartTimeAtFirst))
                    self.logger.info(f'근무 최초 시작')
                    # 프로그램이 종료(근무 끝) 됐을때 총 근무시간 타이머가 종료됨
                    self.totalWorkingCount = timeit.default_timer()
                    # 최초로 근무 유지 시간 계산시..
                    # 두번째 계산부터는 진짜 근무 태만 상태->근무중 전환시에만 근무유지 시간을 초기화한다.
                    self.workStartTime = datetime.now().replace(microsecond=0)
                    self.workCount = timeit.default_timer()
                    self.logger.info(f'근무시작')
                # 근무태만 -> 근무중이 되었을때
                self.alertSlackOff = False
                # 근무태만 시간이 10초 경과 후 재근무 했을 때
                if self.slackOffCount != 0 and (timeit.default_timer() - self.slackOffCount) >= self.NOD_SEC:
                    # 얼마나 근무 태만을 지속했는지 계산(second) (= 근무태만 종료)
                    # 기존 방법 : 근무 태만 유지 시간이 아닌 근무 태만 종료 시점만 계산함
                    # count = timeit.default_timer() - self.slackOffCount
                    # self.totalSlackOffCount += count
                    # delta = timedelta(seconds=count)
                    # calculatedTime = (self.slackOffStartTime + delta).replace(microsecond=0)
                    # self.logger.info("근무 태만 시간은 {0} 부터 {1} 까지 입니다.".format(self.slackOffStartTime, calculatedTime))

                    # 변경방법 : 근무 태만 유지 시간을 계산 (근무 태만 종료 시점은 해당 로그가 찍힌 시점이다.)
                    count = timeit.default_timer() - self.slackOffCount
                    self.totalSlackOffCount += count
                    self.logger.info(f'태만 유지 시간 : ' + str(timedelta(seconds=count)).split(".")[0])

                # 근무 태만 시작을 0으로 초기화
                self.slackOffCount = 0

                # start_time = datetime.now().replace(microsecond=0)
                # self.logger.info("근무 중 : {0}".format(start_time))
                # 근무 유지 시간 측정 시작 (진짜 근무 태만에서 근무중이 될때마다 초기화 됨.
                # but 최초로 근무중일 시에는 위에 최초 근무 시작 시간 저장하는 부분에서 같이 측정)
                if self.isRealSlackOff is True:
                    self.isRealSlackOff = False
                    self.workStartTime = datetime.now().replace(microsecond=0)
                    self.workCount = timeit.default_timer()
                    self.logger.info(f'근무시작')
                self.working = True


            # 프레임 안에 근무자가 없으면 근무태만
            elif self.workerExist == False and self.working == True:
                # 근무태만이 시작된 시간 저장..
                self.slackOffStartTime = datetime.now().replace(microsecond=0)
                self.slackOffCount = timeit.default_timer()

                self.working = False
                # start_time = datetime.now().replace(microsecond=0)
                # self.logger.info("근무 태만 : {0}".format(start_time) )

        for (top, right, bottom, left), name in zip(self.face_locations, self.face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # 얼굴인식 단계가 2단계 이상이라면 사용자의 이름을 표시한다
            if self.RECOG_LV >= 2:
                # cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                pill_image = Image.fromarray(frame)
                draw = ImageDraw.Draw(pill_image)
                draw.rectangle(((left, bottom - 35), (right, bottom)), fill=(0, 0, 225))
                draw.text((left + 30, bottom - 38), name, font=ImageFont.truetype('malgun.ttf', 30), fill=(255, 255, 255))
                frame = np.array(pill_image)
                # font = cv2.FONT_HERSHEY_DUPLEX
                # cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        return frame

    def get_jpg_bytes(self):
        frame = self.get_frame()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        ret, jpg = cv2.imencode('.jpg', frame)
        return jpg.tobytes()

    def calculate_total(self):
        # 진짜 근무 태만인 상태로 끝났을 때에도 해당 태만 시간을 총 태만 시간에 더해주도록 처리함.
        if self.slackOffCount != 0 and (timeit.default_timer() - self.slackOffCount) >= self.NOD_SEC:
            # 얼마나 근무 태만을 지속했는지 계산(second) (= 근무태만 종료)
            # 기존 방법 : 근무 태만 유지 시간이 아닌 근무 태만 종료 시점만 계산함
            # count = timeit.default_timer() - self.slackOffCount
            # self.totalSlackOffCount += count
            # delta = timedelta(seconds=count)
            # calculatedTime = (self.slackOffStartTime + delta).replace(microsecond=0)
            # self.logger.info("근무 태만 시간은 {0} 부터 {1} 까지 입니다.".format(self.slackOffStartTime, calculatedTime))

            # 변경방법 : 근무 태만 유지 시간을 계산 (근무 태만 종료 시점은 해당 로그가 찍힌 시점이다.)
            count = timeit.default_timer() - self.slackOffCount
            self.totalSlackOffCount += count
            self.logger.info(f'태만 유지 시간 : ' + str(timedelta(seconds=count)).split(".")[0])
        else:
            # 마지막에도 근무 유지 시간을 찍어야 함.
            if self.workCount != 0:
                count = timeit.default_timer() - self.workCount
                self.logger.info(f'근무 유지 시간 : ' + str(timedelta(seconds=count)).split(".")[0])

        # 얼굴 인식 아예 안할때 아래 라인에서 문제 생김
        # final_total_working_count = timeit.default_timer() - self.totalWorkingCount

        if self.totalWorkingCount == 0:
            final_total_working_count = 0
        else:
            final_total_working_count = timeit.default_timer() - self.totalWorkingCount

        final_working_count = final_total_working_count - self.totalSlackOffCount
        final_slackoff_count = self.totalSlackOffCount

        total_cnt = str(timedelta(seconds=final_total_working_count)).split(".")[0]
        working_cnt = str(timedelta(seconds=final_working_count)).split(".")[0]
        slack_cnt = str(timedelta(seconds=final_slackoff_count)).split(".")[0]

        final_working_count_int = int(final_working_count)
        final_slackoff_count_int = int(final_slackoff_count)
        final_total_working_count_int = final_slackoff_count_int + final_working_count_int

        self.work_info['total_time'] = final_total_working_count_int
        self.work_info['work_time'] = final_working_count_int
        self.work_info['not_work_time'] = final_slackoff_count_int

        self.logger.info(f'프로그램 종료')
        s = "총근무시간 : "
        if final_total_working_count_int / 60 >= 1:
            s += str(int(final_total_working_count_int / 60)) + "분 "
        s += str(final_total_working_count_int % 60) + "초\n"

        s += "순수근무시간 : "
        if final_working_count_int / 60 >= 1:
            s += str(int(final_working_count_int / 60)) + "분 "
        s += str(final_working_count_int % 60) + "초\n"

        s += "근무태만시간 : "
        if final_slackoff_count_int / 60 >= 1:
            s += str(int(final_slackoff_count_int / 60)) + "분 "
        s += str(final_slackoff_count_int % 60) + "초"

        self.logger.info(f'' + '총근무시간 : ' + total_cnt + ' 순수근무시간 : ' + working_cnt + ' 근무태만시간 : ' + slack_cnt + "\n")
        self.work_info_array.append(self.work_info)

        return s