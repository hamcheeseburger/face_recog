import base64
import cv2
import user_info
import numpy as np


class CheckUser:
    def __init__(self):
        self.known_face_names = []
        self.known_face_images = []
        self.known_face_paths = []
        self.image = []
        self.user_info_array = []

    def convert_txt_to_binary(self):
        with open("test_file.txt", "rb") as f:
            text = f.read()
            print(text)
            print(text.hex())
            print(bytearray.fromhex(text.hex()))

        with open("test_file.bin", "w") as fb:
            fb.write(text.hex())

    def read_binary_file(self):
        with open("test_file.bin", "r") as f:
            data = f.read()
            print(type(data))  # type : str(hex)
            br = bytearray.fromhex(data)

            string = ""
            colum = 0
            image_byte = bytearray()
            info = user_info.UserInfo()

            for b in br:
                ch = chr(b)
                if ch != "," and ch != "\n":
                    if colum != 3:
                        string += ch
                    else:
                        image_byte.append(b)
                else:
                    if colum == 0:  # 사용자 id
                        info.id = string
                    elif colum == 1:  # 사용자 password
                        info.password = string
                    elif colum == 2:  # 사용자 이미지파일명
                        info.name = string
                    elif colum == 3:  # 사용자 이미지파일경로
                        info.image = image_byte
                        print(image_byte)
                        path = 'binary_image/' + info.name + ".jpg"
                        with open(path, 'wb') as image_file:
                            image_file.write(info.image)

                    print(str(colum) + " : " + string)
                    string = ""
                    colum += 1
                    if ch == "\n":
                        self.user_info_array.append(info)
                        info = user_info.UserInfo()  # 새로운 객체
                        colum = 0
                        image_byte = bytearray()
                        print("---")

    def read_images(self):  # read Image file and write to binary file
        # dirname = "knowns"
        # files = os.listdir(dirname)
        # for filename in files:
        #     name, ext = os.path.splitext(filename)
        #     if ext == ".jpg":
        #         self.known_face_names.append(name)
        #         pathname = os.path.join(dirname, filename)
        #
        #         # knowns 폴더에 있는 이미지 파일 가져오기
        #         # self.known_face_images.append(face_recognition.load_image_file(pathname))
        #         print(pathname)
        #         self.known_face_paths.append(pathname)
        #         # img = cv2.imread(pathname)
        #         # self.known_face_images.append(img)

        # dirname = "knowns"
        # files = os.listdir(dirname)
        # for filename in files:
        #     path = os.path.join(dirname, filename)
        with open("knowns/Hwayoung.jpg", "rb") as single_img:
            img_b64 = base64.b64encode(single_img.read()) #type : bytes

        with open("file.bin", "w") as image_binary_file:
            str = img_b64.hex()
            image_binary_file.write(str)
######
        with open('file.bin') as file:
            data = file.read()
            print(data)

        data = bytes.fromhex(data)

        with open("image.jpg", "wb") as image_file:
            image_file.write(data)


    def convert_binary_to_image(self, dt):
        encoded_img = np.fromstring(dt, dtype=np.uint8)
        print(type(encoded_img))
        print(encoded_img)
        # new_byte_img = bytearray(encoded_img)
        # with open("file.bin", "wb") as wf:
        #     wf.write(new_byte_img)
        img = cv2.imdecode(encoded_img, cv2.IMREAD_COLOR)
        cv2.imshow("img", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def test_read_binary(self):
        with open("test_file.txt", "rb") as read_file:
            read_data = read_file.read().decode()

            string = ""
            colum = 0

            info = user_info.UserInfo()
            for d in read_data:
                if d != "," and d != "\n":
                    string += d
                else:
                    if colum == 0:  # 사용자 id
                        info.id = string
                    elif colum == 1:  # 사용자 password
                        info.password = string
                    elif colum == 2:  # 사용자 이미지파일명
                        info.name = string
                    elif colum == 3:  # 사용자 이미지
                        info.path = string
                    print(str(colum) + " : " + string)
                    string = ""
                    colum += 1
                    if d == "\n":
                        self.user_info_array.append(info)
                        info = user_info.UserInfo()  # 새로운 객체
                        colum = 0
                        print("---")

            # print(read_data)

    def match_user(self, user_id, user_pass):
        for info in self.user_info_array:
            if info.id == user_id and info.password == user_pass:
                return info
        return False

    def print_user(self):
        for info in self.user_info_array:
            print(info.id + ", " + info.password + ", " + info.name + "\n")


if __name__ == "__main__":
    user = CheckUser()
    # user.read_images()
    # bi_dt = user.read_binary_file()
    # user.convert_binary_to_image(bi_dt)

    # user.test_read_binary()

    user.read_binary_file()

    id = input("사용자 id를 입력하세요 : ")
    password = input("사용자 password를 입력하세요 : ")

    result = user.match_user(id, password)

    if not result:
        print("로그인 실패")
    else:
        print("로그인 성공")
        # img = cv2.imread(result.path, cv2.IMREAD_COLOR)
        # cv2.imshow("img", img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

    # user.convert_txt_to_binary()

    # user.read_binary_file()
    # user.print_user()

    # user.read_images()
