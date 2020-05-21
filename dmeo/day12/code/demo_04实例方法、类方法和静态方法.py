

# class Data:
#     student_dic = {}
#
#     @classmethod
#     def get_student_dic(cls):
#         """获取学生信息"""
#         return cls.student_dic
#
#     @classmethod
#     def set_student_dic(cls,stu_dic):
#         cls.student_dic = stu_dic

import time
class Views:
    """界面类型"""
    @staticmethod
    def get_current_time():
        #获取当前时间
        now = time.localtime()
        return time.strftime("%Y-%m-%d %H:%M:%S",now)

print(Views.get_current_time())
