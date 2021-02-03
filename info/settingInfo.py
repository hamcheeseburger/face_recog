from realTimeCheck import realtimemain
from videoCheck import videomain2

class SettingInfo:
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
        self.DETEC_SEC = None
        self.NOD_SEC = None
        self.RECOV_LV = None

    def setInfo(self, detec_sec, nod_sec, recov_lv):
        self.DETEC_SEC = detec_sec
        self.NOD_SEC = nod_sec
        self.RECOV_LV = recov_lv
