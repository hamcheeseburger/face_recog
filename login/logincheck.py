# logincheck_유현지_21년01월05일_01시27분
# 로그인을 처리하는 기능


import os
import sqlite3
import pickle


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

        bin_dir = "../user_file"
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


if __name__ == "__main__":
    user = CheckUser()

    user.user_write_binary('yoon', '1234', 'yoon', 'knowns/yoon.jpg')
    user.user_write_binary('현진', '1234', 'Hyeonjin', 'knowns/Hyeonjin.jpg')
    user.user_write_binary('rhj', '1234', 'Hwayoung', 'knowns/Hwayoung.jpg')
    user.user_write_binary('sji', '1234', 'Jaeim', 'knowns/Jaeim.jpg')
    # user.user_check_binary('yjs', '111')
