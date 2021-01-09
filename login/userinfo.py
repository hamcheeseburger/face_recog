"""userinfo
기능설명:
     binary 파일로 로그인을 처리할 때 필요한 dto
개발자:
    유현지
개발일시:
    2021.01.02.20.41.00
버전:
    0.0.1
"""


class UserInfo:
    def __init__(self):
        self.id = ""
        self.password = ""
        self.name = ""
        self.image = bytearray()
