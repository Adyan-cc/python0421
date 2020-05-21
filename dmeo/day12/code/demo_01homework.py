
"""
综合案例：管理员管理课程

- 管理员，添加课程，查看课程 ，删除课程，修改课程
- 分析
  - 数据类Date
    - 属性：课程数据courses_dict，以字典形式保存，类属性
  - 用户类User
    - 属性：用户名，密码，昵称，邮箱，电话
  - 管理员类Admin
    - 属性：继承用户类
    - 方法：添加课程add_course，调用课程保存的方法
      ​	    查看课程check_course，调用数据库类属性
      ​	    修改课程update_course，调用课程修改的方法
      ​	    删除课程delete_course，调用课程删除的方法
  - 课程类Course：
    - 属性：名称，老师，人数限制，课时，学分，课程描述
    - 方法：保存课程
      ​	    修改课程
      ​	    删除课程
      ​	    打印课程信息
"""
#数据类型
class Data:
    """数据类型"""
    courses_dict = {} #键：课程名称，值：课程对象

class User:
    """用户类型"""
    def __init__(self,username,password,nickname,email,phone):
        """初始化属性"""
        self.username = username
        self.password = password
        self.nickname = nickname
        self.email = email
        self.phone = phone

class Admin(User):
    """管理员类"""
    def add_course(self):
        """添加课程"""
        name = input("请输入增加的课程名称：")
        if name in Data.courses_dict:
            print("课程已存在，请使用其他课程名称")
            return self.add_course()
        teacher = input("请输入授课老师：")
        limit = input("请输入人数：")
        times = input("请输入课程时长：")
        score = input("请输入分数：")
        des = input("请输入课程描述：")
        #创建课程对象
        course = Course(name,teacher,limit,times,score,des)
        #保存课程数据
        course.save()

    def check_course(self):
        """查看课程"""
        for name,course in Data.courses_dict.items():
            print(f"课程名称：{name},老师：{course.teacher},课程描述：{course.des}")
        input("课程查看完成，按任意键继续")

    def update_course(self):
        """修改课程"""
        name = input("请输入需要修改的课程名称：")
        if name not in Data.courses_dict:
            print("课程不存在，请重新输入")
            return self.update_course()
        #课程存在，获取课程对象
        course = Data.courses_dict[name]
        course.update()
        input("课程修改完成，按任意键继续。。")
    def delete_course(self):
        """删除课程"""
        name = input("请输入需要删除的课程名称：")
        if name not in Data.courses_dict:
            print("课程不存在，请重新输入")
            return self.delete_course()
        #获取课程对象
        course = Data.courses_dict.get(name)
        course.delete_course()
        input("课程删除完成，按任意键继续。。")

class Course:
    def __init__(self,name,teacher,limit,times,score,des):
        self.name = name
        self.teacher = teacher
        self.limit = limit
        self.times = times
        self.score = score
        self.des = des

    def save(self):
        """保存课程数据"""
        Data.courses_dict[self.name] = self

    def update(self):
        """修改课程"""
        self.teacher = input("请输入修改后的授课老师：")
        self.limit = input("请输入修改后的人数：")
        self.times = input("请输入修改后的课时：")
        self.score = input("请输入修改后的分数：")
        self.des = input("请输入修改后的课程描述：")
        self.save()

    def delete_course(self):
        """删除课程"""
        Data.courses_dict.pop(self.name)

admin = Admin("韩老师","123","韩老师","110@qq.com","12138")
admin.add_course()
admin.check_course()
admin.update_course()
admin.check_course()
admin.delete_course()
admin.check_course()