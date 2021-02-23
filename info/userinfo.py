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
    _instance = None

    @classmethod
    def _getInstance(cls):
        print("UserInfo getInstance()")
        return cls._instance

    @classmethod
    def instance(cls, *args, **kargs):
        print("UserInfo instance()")
        cls._instance = cls(*args, **kargs)
        cls.instance = cls._getInstance
        return cls._instance

    def __init__(self):
        self.id = ""
        self.password = ""
        self.name = ""
        self.image = None
        self.ip = ""
        self.work_time = 0

    def setInfo(self, id, password, name, image, work_time):
        self.id = id
        self.password = password
        self.name = name
        self.image = image
        self.work_time = work_time

