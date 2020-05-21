

class Shopping:
    instance = None #记录创建的对象，None说明是第一次创建对象
    has_init = False #记录是否进行过初始化
    def __new__(cls, *args, **kwargs):
        #第一次调用new方法，创建对象并记录
        #第2-n次调用new方式时，不创建对象，而是直接放回记录的对象

        #判断是否是第一次创建对象
        if cls.instance==None:
            cls.instance = object.__new__(cls)
        return cls.instance

    def __init__(self):
        #单例模式只创建一个对象，所以初始化页应该只执行一次
        if self.has_init==False: #没有进行过初始化
            self.total_price = 31.8
            self.has_init=True