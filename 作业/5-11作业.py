# 1.打开购物车单例模式中，使列表页和详情页价格同步
#
# 2.完善学生选课系统，实现管理员功能即可
"""
数据类Data：
    类属性：
        1.管理员界面跳转数据（可有可无）
        2.课程数据{课程名称：课程对象}
        3.学生用户数据（可有可无）
        4.管理员用户数据（用户名username，密码password,邮箱email,电话phone）
"""
"""

用户类User
    实例属性：用户名username，密码password,邮箱email,电话phone
"""
"""
课程类：Course
    实例属性：（课程coures,老师teacher，人数限制limit，课程描述descripton）
    实例方法：（1.保存课程save 2.修改update  3.删除delete ）
"""
"""
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
    '''数据类'''
    # 保存文章的类属性
    article_dict = dict()
    #管理员登录名
    admini_strator = {"name1": "1","pwd1":'1'}


class User:
    '''实例属性'''
    def __init__(self,username,password,email,phone):
        self.username = username
        self.password = password
        self.email = email
        self.phone =phone

class Course:
    '''实例属性'''
    def __init__(self,coures,teacher,limit,descripton):
        self.coures = coures
        self.teacher = teacher
        self.limit = limit
        self.descripton = descripton

    def save(self):
        ''' 保存课程'''
        Data.article_dict[self.coures] = self

    def update(self):
        '''修改课程'''
        print(self)
        self.coures = input('请修改课程：')
        self.teacher = input('请修改任课老师：')
        self.limit = input('请修改限制人数：')
        self.descripton = input('修改课程描述：')
        # 修改完后重新保存
        self.save()
        min()
    def delete(self):
        '''删除课程'''
        for i in Data.article_dict.keys():
            print(i)
        curriculum_name = input('请输入要删除课程的名称')
        # 调用课程删除方法删除课程
        Data.article_dict[curriculum_name].delete()
        input('按任意键返回')
        min()

    def __str__(self):
        '''打印课程信息'''
        return (f"名称:{self.coures}\n"
                f"老师:{self.teacher}\n"
                f"人数限制:{self.limit}\n"
                f"课程描述:{self.descripton}")

class Admin(User):
    '''管理员类'''

    def add_course(self):
        '''添加课程'''
        article_dict = list()
        for key in ['课程名称', '任教老师', '人数限制', '课程描述']:
            a = input(f'请输入{key}')
            article_dict.append(a)
        curriculum = Course(*article_dict)
        curriculum.save()
        input('课程增加成功，按任意键打印增加课程的信息')
        print(curriculum)
        input('按任意键返回')
        min()

    def check_course(cls, *args, **kwargs):
        ''' 查看课程'''
        # 课程就是数据里的值
        for i in Data.article_dict.values():
            print(i)
        input('按任意键返回')
        min()


def min():
    name = input('请输入账户:')
    pwd = input('请输入密码:')
    if Data.admini_strator["name1"] == name and pwd == Data.admini_strator["pwd1"]:
        print('登录成功')
        shouye_dict = {'1': 'qwe.add_course()', '2': 'qwe.check_course()',
                       '3': 'qwr.update()', '4': 'qwr.delete()','5':'exit()'}
        print(' ='*15)
        print(' '*7,'1.增加课程')
        print(' '*7,'2.查看课程')
        print(' '*7,'3.修改课程')
        print(' '*7,'4.删除课程')
        print(' '*7,'5.退出系统')
        print(' =' * 15)
        choose = input("请输入选项")
        eval(shouye_dict[choose])
    else:
        print('输入错误，任意键返回。。。。')
        min()

qwr = Course(1,1,1,1)
qwe = Admin(1,1,1,1)
min()