

# 需求：声明一个普通用户类型，类型包含用户名，密码，昵称，有保存和删除的方法

class User:
    """用户类型"""
    def __init__(self):
        """记录用户属性"""
        self.username = "张伟强"
        self.password = "123"
        self.nickname = "强哥"

    def save(self):
        """保存方法"""
        pass

    def delete(self):
        """删除方法"""
        pass