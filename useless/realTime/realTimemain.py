"""realTime Main (useless)
기능설명:
     새로운 로그인 시스템에 연결하기 위해서 추가해야 할 항목들이 있었기에 새롭게 파일을 만들었음
     (이 파일은 로그인기능이 생기기 이전의 파일)
개발자:
    송재임, 유현지
개발일시:
    2021.01.05.23.04.00
버전:
    0.0.2
"""
# face_recog.py
# 얼굴인식 기능에 초점을 맞춘 wrapper 패키지
import math

import face_recognition
import cv2
import os
import numpy as np
# 파이썬은 B,G,R형태(numpy객체)로 이미지를 표현
# OpenCV: [B, G, R]

import logging
from realTimeCheck import camera


class FaceRecog:

    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.

        # 근무 중임을 나타내는 boolean 변수
        self.working = False
        # 화면에 잡힌 얼굴중 근무자가 존재하는지를 알아내는 boolean 변수
        self.workerExist = False

        self.paused = False

        # test_video2.mp4 : 노트북 웹캠 영상
        # test_video3.mp4 : 핸드폰 촬영 영상
        # test_video4.mp4 : 유튜브 영상(2인 이상 출현)

        # 카메라 버전으로 테스트시 camera 모듈 사용!!
        self.video = camera.VideoCamera()
        # self.video = cv2.VideoCapture('./video/video_test3.mp4')

        self.name = ''
        self.known_face_encodings = []
        self.known_face_names = []
        self.frame_count = 0

        # 근무 최초 시작시간 초기화
        self.workStartTimeAtFirst = 0
        # 총 근무 시간 초기화 (계산전 : 근무 최초 시작 이래 무조건 계속 증가..근무 종료시에 - totalSlcakOffCount)
        self.totalWorkingCount = 0
        # 근무 태만 시작시간 초기화
        self.slackOffStartTime = 0
        # 근무 태만 시간 초기화 (재근무 시 마다 초기화)
        self.slackOffCount = 0
        # 근무 태만 10초 이상시 근무태만이 시작되었다는 것을 알려주었는지 체크(무한 print 방지)
        self.alertSlackOff = False
        # 총 근무 태만 시간 초기화 (재근무 시 마다 + slackOffCount )
        self.totalSlackOffCount = 0

        # 로그 파일 생성 준비

        # logger instance 생성
        self.logger = logging.getLogger(__name__)
        # handler 생성 (stream, file)
        streamHandler = logging.StreamHandler()
        fileHandler = logging.FileHandler('../../server.log')
        # logger instance에 handler 설정
        self.logger.addHandler(streamHandler)
        self.logger.addHandler(fileHandler)
        # logger instance로 log 찍기
        self.logger.setLevel(level=logging.DEBUG)

        # Load sample pictures and learn how to recognize it.
        # knowns 디렉토리에서 사진 파일을 읽습니다. 파일 이름으로부터 사람 이름을 추출합니다.
        dirname = 'user_image'
        files = os.listdir(dirname)
        filename = files[0]
        name, ext = os.path.splitext(filename)
        self.name = name
        if ext == '.jpg':
            self.known_face_names.append(name)
            pathname = os.path.join(dirname, filename)
            img = face_recognition.load_image_file(pathname)  # 이미지파일 가져오는 코드..
            face_encoding = face_recognition.face_encodings(img)[0]
            self.known_face_encodings.append(face_encoding)
        # Load sample pictures and learn how to recognize it.
        # knowns 디렉토리에서 사진 파일을 읽습니다. 파일 이름으로부터 사람 이름을 추출합니다.
        dirname = 'knowns'
        files = os.listdir(dirname)
        for filename in files:
            name, ext = os.path.splitext(filename)
            if ext == '.jpg':
                self.known_face_names.append(name)
                pathname = os.path.join(dirname, filename)

                # 사진에서 얼굴 영역을 알아내고, face landmarks라 불리는 68개 얼굴 특징의 위치를 분석한 데이
                # 터를 known_face_encodings에 저장합니다. 이 작업의 원리는 이 사이트
                # (https://medium.com/@jongdae.lim/%EA%B8%B0%EA%B3%84-%ED%95%99%EC%8A%B5-machine-learning-
                # %EC%9D%80-%EC%A6%90%EA%B2%81%EB%8B%A4-part-4-63ed781eee3c)에 잘 설명되어 있습니다. 아주 쉽게
                # 설명되어 있으므로, 꼭 한 번 읽어보시길 강력 추천 드립니다.

                img = face_recognition.load_image_file(pathname)
                face_encoding = face_recognition.face_encodings(img)[0]
                self.known_face_encodings.append(face_encoding)

        # Initialize some variables
        # 왜 리스트? 한 프레임에 얼굴이 여러개 일 수 있으니까?
        self.face_locations = []
        self.face_encodings = []
        self.face_names = []
        self.process_this_frame = True
        self.video_end = False

        self.first = True
        self.totalFrame = 0
        self.recogFrame = 0
        self.notRecogFrame = 0

        self.FPS = 30
        self.standard = 10

    # 근무여부를 확인하는 boolean 변수를 반환한다.
    @property
    def working(self):
        return self._working

    @working.setter
    def working(self, value):
        self._working = value

    def __del__(self):
        del self.video

    def get_name(self, name):
        self.name = name
        print(self.name)

    def notifyIsPaused(self, paused):
        self.paused = paused

    def get_frame(self):
        # 카메라 버전으로 테스트시
        frame = self.video.get_frame()
        # ret, frame = self.video.read()

        if frame is None:
            self.video_end = True
            #  return None 으로 바꿔야 함!!!!!
            return None
        # 카메라로부터 frame을 읽어서 1/4 크기로 줄입니다. 이것은 계산양을 줄이기 위해서 입니다.
        # Grab a single frame of video
        # Resize frame of video to 1/4 size for faster face recognition processing
        self.totalFrame += 1;  # 전체프레임갯수

        # 0.33초마다 얼굴인식 0~600 0 10 20 ...
        if self.totalFrame % 10 == 0:
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            rgb_small_frame = small_frame[:, :, ::-1]
            # 계산 양을 더 줄이기 위해서 두 frame당 1번씩만 계산합니다.
            # Only process every other frame of video to save time
            if self.process_this_frame:
                # Find all the faces and face encodings in the current frame of video
                # 프레임 안에 존재하는 모든 얼굴의 위치를 가져오고, 해당 얼굴들의 특징을 추출한다.
                self.face_locations = face_recognition.face_locations(rgb_small_frame)
                self.face_encodings = face_recognition.face_encodings(rgb_small_frame, self.face_locations)

                self.face_names = []
                for face_encoding in self.face_encodings:
                    # See if the face s a match for the known face(s)
                    # Frame에서 추출한 얼굴 특징과 knowns에 있던 사진 얼굴의 특징을 비교하여, (얼마나 비슷한지)
                    # 거리 척도로 환산합니다. 거리(distance)가 가깝다는 (작다는) 것은 서로 비슷한 얼굴이라는 의미입니다.
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
            ############

            # Display the results
            # 찾은 사람의 얼굴 영역과 이름을 비디오 화면에 그립니다.
            # 프레임 안에 얼굴이 없으면(근무지 이탈) '근무 태만'
            if len(self.face_locations) == 0:
                # 근무태만이 시작된 시간 저장..
                if self.working:  # 얼굴인식이 되다가 안되기 시작한 첫 번째 순간
                    self.notRecogFrame = 0  # 얼굴인식이 안됐을 때 프레임 갯수 300장 = 10초
                else:  # 계속 얼굴 인식이 안되는 순간
                    self.notRecogFrame += 10
                self.working = False

            else:
                # 프레임 안에 얼굴이 있되, 근무자가 있는 경우와 없는 경우를 구분
                # 일단 프레임안에 얼굴이 존재하면, workerExist = False 초기화
                self.workerExist = False
                for face_name in self.face_names:
                    # 해당 조건문을 사용자 입력값으로 받으면 원하는 사람의 근무여부만 체크할 수 있지 않을까?
                    if face_name == self.name:
                        self.workerExist = True
                        break

                if self.workerExist:
                    if self.notRecogFrame < 10 * self.FPS:  # 300장
                        # 인식이 됐을 때 프레임 갯수
                        self.recogFrame += self.notRecogFrame
                    else:
                        print("근무태만: 10초 지남")
                    self.recogFrame += 10

                # 얼굴 인식이 안되다가 인식이 된 순간
                if self.workerExist and not self.working:
                    count = round(self.totalFrame / self.FPS)
                    if count == 0 and self.first:
                        print("근무시작")
                        self.first = False
                    else:
                        print("인식이 되지 않은 시간 : " + str(round(self.notRecogFrame / self.FPS)) + "초")
                        print("근무중 : " + str(count) + "초 경과")
                        self.notRecogFrame = 0
                    self.working = True

            for (top, right, bottom, left), name in zip(self.face_locations, self.face_names):
                # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                # Draw a box around the face
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

                # Draw a label with a name below the face
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        return frame

    def get_jpg_bytes(self):
        frame = self.get_frame()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        ret, jpg = cv2.imencode('.jpg', frame)
        return jpg.tobytes()

    # def calculate_total(self):
    #     # 30fps라고 가정
    #     print("전체 프레임 : " + str(self.totalFrame));
    #     print("인식된 프레임 : " + str(self.recogFrame));
    #     totalTime = round(self.totalFrame / self.FPS);
    #     recogTime = round((self.recogFrame / self.totalFrame) * totalTime)
    #     self.logger.info("\n---------프로그램 종료----------")
    #     s = "총근무시간 : " + str(totalTime) + "초\n" + "근무시간 : " + str(recogTime) + "초\n" + "태만시간 : " + str(
    #         totalTime - recogTime) + "초\n";
    #     print(s)
    #     return s

    # 실제 근무 시간의 절반 정도로만 근무시간으로 인정하는 듯??
    def calculate_total(self):
        # 영상 마지막에 근무자가 인식이 되지 않는다면 태만시간에 대한 계산이 끝나지 않으므로
        # 영상이 마친 후 계산을 한번 더 해준다.
        print(self.first)
        # if self.notRecogFrame != 0 and self.first is False:
        if self.notRecogFrame != 0 and self.notRecogFrame / self.FPS < 10:
            print("인식이 되지 않은 시간 : " + str(round(self.notRecogFrame / self.FPS, 1)) + "초")
            self.recogFrame += self.notRecogFrame
            self.notRecogFrame = 0

        # 근무시간 계산
        totalTime = round(self.totalFrame / self.FPS);
        totalTimeM = math.trunc(totalTime / 60)
        recogTime = round((self.recogFrame / self.totalFrame) * totalTime)
        recogTimeM = math.trunc(recogTime / 60)
        notRecogTime = totalTime - recogTime

        # 총태만시간이 10초 미만일 수는 없다.
        if notRecogTime < 10:
            recogTime += notRecogTime
            notRecogTime = 0

        notRecogTimeM = math.trunc(notRecogTime / 60)

        self.logger.info("\n---------프로그램 종료----------")
        print("동영상 fps : " + str(self.FPS))
        print("전체 프레임 : " + str(self.totalFrame));
        print("인식된 프레임 : " + str(self.recogFrame));
        s = "총근무시간 : " + str(totalTimeM) + "분 " + str(totalTime - totalTimeM * 60) + "초\n" \
            + "근무시간 : " + str(recogTimeM) + "분 " + str(recogTime - recogTimeM * 60) + "초\n" \
            + "태만시간 : " + str(notRecogTimeM) + "분 " + str(notRecogTime - notRecogTimeM * 60) + "초\n";
        print(s)
        return s


if __name__ == '__main__':
    face_recog = FaceRecog()
    print(face_recog.known_face_names)
    while True:
        if face_recog.video_end:
            break;
        frame = face_recog.get_frame()

        # show the frame
        # cv2.imshow(title(윈도우창 제목), image(출력할 이미지 객체))//특정한 이미지를 화면에 출력
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

        # if the `q` key was pressed, break from the loop
        if key == ord('q'):
            break

    # do a bit of cleanup

    cv2.destroyAllWindows()
    face_recog.calculate_total()
    print('finish')
