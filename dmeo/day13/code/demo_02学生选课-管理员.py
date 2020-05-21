

"""
数据类Data：
    类属性：
        1.管理员界面跳转数据（可有可无）
        2.课程数据{课程名称：课程对象}
        3.学生用户数据（可有可无）
        4.管理员用户数据（用户名username，密码password,邮箱email,电话phone）

用户类User
    实例属性：用户名username，密码password,邮箱email,电话phone

课程类：Course
    实例属性：（课程coures,老师teacher，人数限制limit，课程描述descripton）
    实例方法：（1.保存课程save 2.修改update  3.删除delete ）

管理员类：Admin，继承User
    实例方法：（1.界面展示，选择功能admin_page 2.添加add_course,3.查看check_course4.修改update_course,5.删除delete_course,6.退出system_exit）

	界面展示如下：
        print("         1.查看课程")
        print("         2.添加课程")
        print("         3.删除课程")
        print("         4.修改课程")
        print("         5.退出系统")

定义主函数main()
    输入管理员账号和密码，创建管理员对象，调用管理员方法(根据用户输入序号，调用相应方法)

以上仅供参考，但要和函数实现管理员功能效果基本一致
"""

class Data:
    #管理员跳转，字典
    admin_page_dict = {
        "1":"self.check_course()" ,#管理员查看课程
        "2": "self.add_course()",
        "3": "self.delete_course()",
        "4": "self.update_course()",
        "5": "self.system_exit()",
    }

    #课程数据
    course_dic = {}

    #管理员数据
    admin_dic = {"username":"admin","password":"admin","email":"110@qq.com","phone":12138}

# 用户类User
#     实例属性：用户名username，密码password,邮箱email,电话phone
class User:
    """用户类"""
    def __init__(self,username,password,email,phone):
        self.username = username
        self.password = password
        self.email = email
        self.phone = phone

# 课程类：Course
#     实例属性：（课程coures,老师teacher，人数限制limit，课程描述descripton）
#     实例方法：（1.保存课程save 2.修改update  3.删除delete ）

class Course:
    def __init__(self,course,teacher,limit,des):
        self.course = course
        self.teacher = teacher
        self.limit = limit
        self.des = des

    def sava(self):
        """保存课程"""
        Data.course_dic[self.course] = self #字典的值是课程对象
        input(f"您已成功操作{self.course},按任意键返回")

    def delete(self):
        """删除课程"""
        #通过key删除字典中的一个键值对
        Data.course_dic.pop(self.course)

    def update(self):
        """修改课程"""
        self.teacher = input("请输入任课老师：")
        self.limit =  input("请输入人数限制：")
        self.des = input("请输入课程描述：")
        self.sava()

# 管理员类：Admin，继承User
#     实例方法：（1.界面展示，选择功能admin_page 2.添加add_course,3.查看check_course
# 4.修改update_course,5.删除delete_course,6.退出system_exit）
# 	界面展示如下：
#         print("         1.查看课程")
#         print("         2.添加课程")
#         print("         3.删除课程")
#         print("         4.修改课程")
#         print("         5.退出系统")

class Admin:
    def admin_page(self):
        print("="*30)
        print("         1.查看课程")
        print("         2.添加课程")
        print("         3.删除课程")
        print("         4.修改课程")
        print("         5.退出系统")
        print("=" * 30)

        #提示用户输入功能选项
        choose = input("请输入功能选项：") #1,2,3,4,5
        ret = Data.admin_page_dict.get(choose,"self.admin_page")
        ret2 = eval(ret)
        if ret2 !=None:
            return eval(ret2)

    def add_course(self):
        """添加课程"""
        add_course = input("请输入要添加的课程名称：")
        if add_course in Data.course_dic:
            input(f"您添加的{add_course}课程已存在，按任意键返回上一级")
        else:
            teacher = input("请输入任课老师：")
            limit = input("请输入人数限制：")
            des = input("请输入课程描述：")
            course = Course(add_course,teacher,limit,des)
            course.sava()
        return "self.admin_page()"

    def check_course(self):
        """查看课程"""
        for k,v in Data.course_dic.items():
            print(f"课程名称:{v.course},授课老师:{v.teacher},人数:{v.limit},课程描述:{v.des}")
        input("按任意键返回")
        return "self.admin_page()"

    def update_course(self):
        """修改课程"""
        for k,v in Data.course_dic.items():
            print(f"课程名称:{v.course},授课老师:{v.teacher},人数:{v.limit},课程描述:{v.des}")
        name = input("请输入要修改的课程名称：")
        if name not in Data.course_dic:
            print("课程不存在,请重新输入")
            return self.update_course()
        update_course = input("请输入修改后的课程名称")
        course = Data.course_dic.get(name)
        Data.course_dic.pop(name)
        course.course = update_course
        course.update()
        input("修改成功，按任意键返回上一级")
        return "self.admin_page()"

    def delete_course(self):
        for k,v in Data.course_dic.items():
            print(f"课程名称:{v.course},授课老师:{v.teacher},人数:{v.limit},课程描述:{v.des}")
        #输入删除的课程名称
        rem_course = input("请输入要删除的课程名称：")
        if rem_course in Data.course_dic:
            course = Data.course_dic.get(rem_course)
            course.delete()
            input("删除课程成功，按任意键返回上一级")
            return "self.admin_page()"
        else:
            input("课程不存在，按任意键返回")
            return "self.admin_page()"

    def system_exit(self):
        exit(1)

def main():
    print("=====欢迎来到管理员后台=====")
    username = input("请输入管理员账号：")
    password = input("请输入管理员密码：")
    data_admin = Data.admin_dic.get("username")
    data_password = Data.admin_dic.get("password")
    if username==data_admin and password==data_password:
        admin = Admin()
        admin.admin_page()
    else:
        input("账号或密码错误")
        return main()
main()
