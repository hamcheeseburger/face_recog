import sqlite3
import base64

class CheckUserDB:
    def createDB(self):
        conn = sqlite3.connect("recog_user.db", isolation_level=None)
        cursor = conn.cursor()
        cursor.execute(
            "CREATE TABLE user_table (id TEXT PRIMARY KEY, password TEXT, name TEXT, image BLOB)"
        )
        cursor.close()
        conn.close()

    def findUser(self, id, password):
        conn = sqlite3.connect("recog_user.db", isolation_level=None)
        cursor = conn.cursor()

        sql = "select name, hex(image) from user_table where id=? and password=?"
        cursor.execute(sql, (id, password))
        row = cursor.fetchone()
        if row is None:
            return False

        print(row[0]) # 사용자 이름
        strr = row[1] # 사용자 사진

        with open('test_file.bin', 'a') as file_bin:
            file_bin.write(strr)

        path = "db_image/" + row[0] + ".jpg"
        print(path)
        with open(path, 'wb') as file:
            file.write(bytes.fromhex(strr))

        cursor.close()
        conn.close()

        return True


if __name__ == "__main__":
    userdb = CheckUserDB()
    # userdb.createDB()

    id = input("사용자 id를 입력하세요 : ")
    password = input("사용자 password를 입력하세요 : ")

    if userdb.findUser(id, password):
        print("로그인 성공")
    else:
        print("로그인 실패")
