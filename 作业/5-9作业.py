# 综合案例：管理员管理课程
# - 管理员，添加课程，查看课程 ，删除课程，修改课程
# - 分析
#   - 数据类
#     - 属性：课程数据courses_dict，以字典形式保存，类属性
#   - 用户类
#     - 属性：用户名，密码，昵称，邮箱，电话
#   - 管理员类
#     - 属性：继承用户类
#     - 方法：添加课程add_course，调用课程保存的方法
#       ​	    查看课程check_course，调用数据库类属性
#       ​	    修改课程update_course，调用课程修改的方法
#       ​	    删除课程delete_course，调用课程删除的方法
#   - 课程类：
#     - 属性：名称，老师，人数限制，课时，学分，课程描述
#     - 方法：保存课程
#       ​	    修改课程
#       ​	    删除课程
#       ​	    打印课程信息

class Data:
    '''数据类'''
    # 保存文章的类属性
    article_dict = dict()


class User:
    '''用户类'''
    def __init__(self,user_name,password,nickname,mailbox,telephone):
        '''属性：用户名，密码，昵称，邮箱，电话'''
        self.user_name = user_name
        self.password = password
        self.nickname = nickname
        self.mailbox = mailbox
        self.telephone = telephone


class Admin(User):
    '''管理员类'''

    def add_course(self):
        '''添加课程'''
        article_dict = list()
        for key in ['课程名称','任教老师','人数限制','课时','课程的学分','课程描述'] :
            a = input(f'请输入{key}')
            article_dict.append(a)
        curriculum = Curriculum(*article_dict)
        curriculum.addcourse()
        input('课程增加成功，按任意键打印增加课程的信息')
        print(curriculum)
        input('按任意键返回')
        shouye()

    def check_course(cls, *args, **kwargs):
        ''' 查看课程'''
        # 课程就是数据里的值
        for i in Data.article_dict.values():
            print(i)
        input('按任意键返回')
        shouye()

    def update_course(self):
        '''修改课程'''
        for i in Data.article_dict.keys():
            print(i)
        curriculum_name = input('请输入要修改课程的名称')
        # 调用课程修改方法
        res = Data.article_dict[curriculum_name].modify()
        # 打印修改后课程信息
        input('按任意键打印课程信息')
        print(res)
        input('按任意键返回')
        shouye()

    def delete_course(self):
        '''删除课程'''
        for i in Data.article_dict.keys():
            print(i)
        curriculum_name = input('请输入要删除课程的名称')
        # 调用课程删除方法删除课程
        Data.article_dict[curriculum_name].delete()
        input('按任意键返回')
        shouye()

class Curriculum:
    '''课程类'''

    def __init__(self, name, teacher, number, class_hour, credit, describe):
        '''属性：名称，老师，
        人数限制，课时，学分，课程描述'''
        self.name = name
        self.teacher = teacher
        self.number = int(number)
        self.class_hour = class_hour
        self.credit = credit
        self.describe = describe

    def addcourse(self):
        ''' 保存课程'''
        Data.article_dict[self.name] = self

    def modify(self):
        '''修改课程'''
        print(self)
        self.teacher = input('请修改任课老师')
        self.num_limit = input('请修改限制人数')
        self.course_time = input('请修改课时')
        self.course_score = input('请修改学分')
        self.description = input('修改课程描述')
        # 修改完后重新保存
        self.addcourse()
        return self

    def delete(self):
        '''删除课程'''
        Data.article_dict.pop(self.name)

    def __str__(self):
        '''打印课程信息'''
        return (f"名称:{self.name}\n"
                f"老师:{self.teacher}\n"
                f"人数限制:{self.number}\n"
                f"课时:{self.class_hour}\n"
                f"学分:{self.credit}\n"
                f"课程描述:{self.describe}")




def shouye():
    shouye_dict = {'1': 'qwe.add_course()', '2': 'qwe.check_course()',
                   '3': 'qwe.update_course()',' "4"': 'qwe.delete_course()','5':'exit()'}
    print(' ='*15)
    print(' '*7,'1.增加课程')
    print(' '*7,'2.查看课程')
    print(' '*7,'3.修改课程')
    print(' '*7,'4.删除课程')
    print(' '*7,'5.退出系统')
    print(' =' * 15)
    choose = input("请输入选项")
    eval(shouye_dict[choose])


qwe = Admin("1",1,1,1,1)
shouye()