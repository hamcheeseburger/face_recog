import datetime


class WorkInfo:
    def __init__(self):
        self.date_time = datetime.datetime.now()  # 날짜시간
        self.total_time = None  # 총근무시간
        self.work_time = None  # 순수근무시간
        self.not_work_time = None  # 태만시간
        self.work_type = None  # 실시간인식인지, 비디오인식인지의 구분값


class ArrayWorkInfo:
    _instance = None

    @classmethod
    def _getInstance(cls):
        return cls._instance

    @classmethod
    def instance(cls, *args, **kargs):
        cls._instance = cls(*args, **kargs)
        cls.instance = cls._getInstance
        return cls._instance

    def __init__(self):
        self.work_info_array = []
