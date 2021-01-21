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

import os
import sqlite3
import pickle

import pymysql
import requests


class CheckUser:
    def __init__(self):
        self.known_face_names = []
        self.known_face_images = []
        self.known_face_paths = []
        self.image = []
        self.user_info_array = []

    def user_write_binary(self, id, password, name, path):
        with open(path, "rb") as img:
            img_byte = img.read()

        MyObject = {'id': id,
                    'password': password,
                    'name': name,
                    'image': img_byte
                    }

        bin_dir = "./user_file"
        bin_file_name = "user_" + id + "_" + name + ".txt"
        bin_path = bin_dir + "/" + bin_file_name
        with open(bin_path, "wb") as MyFile:
            pickle.dump(MyObject, MyFile, protocol=3)

    def user_check_binary(self, id, password):
        dirname = 'user_file'
        files = os.listdir(dirname)

        for filename in files:
            path = dirname + '/' + filename
            with open(path, "rb") as MyFile:
                read_obj = pickle.load(MyFile)
                if read_obj['id'] == id and read_obj['password'] == password:
                    print("로그인 성공")
                    url = "user_image/" + read_obj['name'] + ".jpg"
                    with open(url, "wb") as WriteFile:
                        WriteFile.write(read_obj['image'])
                    return True

        print("로그인 실패")
        return False

    def user_check_db(self, id, password):
        conn = sqlite3.connect("recog_user.db", isolation_level=None)
        cursor = conn.cursor()

        sql = "select name, hex(image) from user_table where id=? and password=?"
        cursor.execute(sql, (id, password))
        row = cursor.fetchone()
        if row is None:
            return False

        print(row[0])  # 사용자 이름
        strr = row[1]  # 사용자 사진

        path = "user_image/" + row[0] + ".jpg"
        print(path)
        with open(path, 'wb') as file:
            file.write(bytes.fromhex(strr))

        cursor.close()
        conn.close()
        return True

    def user_check_aws(self, id, pswd):
        host = "face-recog-db-dev.ckeffyuykcfz.ap-northeast-2.rds.amazonaws.com"
        port = 3306
        username = "admin"
        database = "mydb"
        password = "12345678"

        conn = pymysql.connect(host=host, user=username, passwd=password, db=database, port=port, charset='utf8')
        cursor = conn.cursor()
        query = "select name, hex(image) as img from member where login_id=%s and password=%s"
        cursor.execute(query, (id, pswd))
        row = cursor.fetchone()

        if row is None:
            print("no data")
            return False
        else:
            print(row[0])
            strr = row[1]  # 사용자 사진

            path = "user_image/" + row[0] + ".jpg"
            print(path)
            with open(path, 'wb') as file:
                file.write(bytes.fromhex(strr))

        cursor.close()
        conn.close()
        return True

    def user_check_web_server(self, id, password):
        info = {
            'login_id' : id,
            'password' : password
        }

        url = "http://localhost:8080/awsDBproject/user/login"
        response = requests.post(url, data=info)

        print(response)

if __name__ == "__main__":
    user = CheckUser()

    # user.user_write_binary('사용자아이디', '비밀번호', '사용자이름', '이미지경로')

    # 예시
    # user.user_write_binary('yhj', '1234', 'Hyeonji', 'knowns/Hyeonji.jpg')

    # user.user_check_aws('yhj', '1234')

    user.user_check_web_server('yhj', '1234')