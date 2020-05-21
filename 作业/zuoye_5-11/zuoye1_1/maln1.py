
# 2.完善学生选课系统，实现管理员功能即可
"""
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





'''程序入口'''
from 作业.zuoye01.zuoye.views import shou_ye
shou_ye()




