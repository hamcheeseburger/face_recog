class LogInfo:
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
        self.file_name = ""
        self.context_path = "./worklog/"
        self.file_path = ""
        self.created_date = ""

    def setFileName(self, f_n):
        self.file_name = f_n
        self.file_path = self.context_path + self.file_name
