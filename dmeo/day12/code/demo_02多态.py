

# #定义人类：可以跳舞，可以玩，在玩的过程中跳舞
# #实现多态：老年人跳广场舞
# class Person:
#     """人的类型"""
#
#     def dance(self):
#         print("跳舞")
#
#     def play(self):
#         self.dance()
#
# class OldMan(Person):
#     """老年人类型"""
#     def dance(self):
#         print("跳广场舞")
#
# # per1 = Person()
# # per1.play()
# old = OldMan()
# old.play()




# - 网站类
#   - 方法：注册方法，调用默认设备发送验证码
# - 设备类
#   - 方法：生成验证码并发送

# class WebSite:
#     """网站类型"""
#     def register(self,device):
#         print("开始注册用户。。。")
#         #调用设备发送验证码的方法
#         device.send("6666")
#         input("验证码已发送，请输入：")
#         print("注册成功")
#
# class Device:
#     """设备类型"""
#     def send(self,code):
#         print("默认发送验证码:",code)
#
# #用户注册
# ws = WebSite()
# device = Device()
# #发起注册
# ws.register(device)



# 实现多态，用不同的设备注册网站，就使用相应的设备发送验证码
class WebSite:
    """网站类型"""
    def register(self,device):
        print("开始注册用户。。。")
        #调用设备发送验证码的方法
        device.send("6666")
        input("验证码已发送，请输入：")
        print("注册成功")

class Device:
    """设备类型"""
    def send(self,code):
        print("默认发送验证码:",code)

class Phone(Device):
    """手机注册"""
    def send(self,code):
        print("通过手机发送验证码：",code)

class Email:
    """邮箱注册"""
    def send(self, code):
        print("通过邮箱发送验证码：", code)

#用户注册
ws = WebSite()
# device = Device()
phone = Phone()
#发起注册
ws.register(phone)
