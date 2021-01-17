import os

import face_recognition


class Knowns:
    _instance = None

    @classmethod
    def _getInstance(cls):
        print("[getknowns.py] _getInstance call")
        return cls._instance

    @classmethod
    def instance(cls, *args, **kargs):
        print("[getknowns.py] instance call")
        cls._instance = cls(*args, **kargs)
        cls.instance = cls._getInstance
        return cls._instance

    def __init__(self):
        self.known_face_encodings = []
        self.known_face_names = []

        print("[getknowns.py] __init__")
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

                img = face_recognition.load_image_file(pathname)  # 이미지파일 가져오는 코드..
                face_encoding = face_recognition.face_encodings(img)[0]
                self.known_face_encodings.append(face_encoding)

