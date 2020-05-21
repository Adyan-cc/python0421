

class Shopping:
    instance = None #记录创建的对象，None说明是第一次创建对象
    def __new__(cls, *args, **kwargs):
        #第一次调用new方法，创建对象并记录
        #第2-n次调用new方式时，不创建对象，而是直接放回记录的对象

        #判断是否是第一次创建对象
        if cls.instance==None:
            cls.instance = object.__new__(cls)
        return cls.instance

    def __init__(self):
        self.total_price = 31.8