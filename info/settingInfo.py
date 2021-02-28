
class SettingInfo:
    _instance = None

    @classmethod
    def _getInstance(cls):
        print("SettingInfo getInstance()")
        return cls._instance

    @classmethod
    def instance(cls, *args, **kargs):
        print("SettingInfo instance()")
        cls._instance = cls(*args, **kargs)
        cls.instance = cls._getInstance
        return cls._instance

    def __init__(self):
        self.DETEC_SEC = 0
        self.NOD_SEC = 0
        self.RECOV_LV = 0
        self.VID_INTVL = 0

    def reset(self, detec_sec, nod_sec, recog_lv, vid_intvl):
        self.DETEC_SEC = detec_sec
        self.NOD_SEC = nod_sec
        self.RECOV_LV = recog_lv
        self.VID_INTVL = vid_intvl
