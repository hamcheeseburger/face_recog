"""login Check
기능설명:
     로그인을 처리하는 기능 모듈
개발자:
    유현지
개발일시:
    2021.01.05.01.27.00
버전:
    0.0.1
"""
import base64
import os
import sqlite3
import pickle

import pymysql
import requests


class CheckUser:
    # URL = "http://localhost:8090/awsDBproject/user/login"
    URL = "http://3.35.38.165:8080/awsDBproject/user/login"

    def __init__(self):
        self.known_face_names = []
        self.known_face_images = []
        self.known_face_paths = []
        self.image = []
        self.user_info_array = []

    def user_check_web_server(self, id, password):
        info = {
            'login_id': id,
            'password': password
        }

        # putty 접속하여 tomcat 서버 구동한 후 테스트 할 것
        # url = "http://3.35.38.165:8080/awsDBproject/user/login"
        print(self.URL)
        try:
            response = requests.post(self.URL, data=info, verify=False)
        except:
            print("Connection Error")
            return -2, None, None

        print(response.status_code)
        # 추후 fail.jsp에서는 응답 코드를 200이 아닌 것으로 바꾸는 것으로?
        if response.status_code == 200:
            # json 응답일 경우 딕셔너리로 변환
            json_data = response.json()
            if json_data.get("error"):
                print(json_data['error'])
                return 0, None, None

            if json_data.get('image') and json_data.get('name'):
                # Encoding 후 member_image 타입은 bytes
                member_image = base64.b64decode(json_data['image'])
                member_name = json_data['name']
                # print("Welcome " + member_name + "!!")

                return 1, member_name, member_image
        else:
            print("response error")
            return -1, None, None


if __name__ == "__main__":
    user = CheckUser()

    # user.user_write_binary('사용자아이디', '비밀번호', '사용자이름', '이미지경로')

    # 예시
    # user.user_write_binary('yhj', '1234', 'Hyeonji', 'knowns/Hyeonji.jpg')

    # user.user_check_aws('yhj', '1234')

    user.user_check_web_server('sji', '1234')
