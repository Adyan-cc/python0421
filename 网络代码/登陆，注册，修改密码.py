import os


def login(username, password):
    f = open("db", 'r')
    for line in f:
        # print(line,tBlank spaceype(line))
        line_list = line.strip().split("|")
        # print(line_list,type(line_list))
        if line_list[0] == username and line_list[1] == password:
            return True
    return False


def register(username, password):
    f = open("db", 'a')
    temp = "\n" + username + "|" + password
    f.write(temp)
    f.close()
    return True


def change_pwd(username):
    new_pwd = input('请输入新的密码：')
    write_flag = False

    with open('db', 'r', encoding='utf-8') as old_file, open('db_new', 'w', encoding='utf-8') as new_file:
        for line in old_file:
            if username == line.strip().split('|')[0] and new_pwd != line.strip().split('|')[1]:
                line_list = line.strip().split('|')  # 把字符串分割成列表
                # print(line_list, type(line_list))  # 输出['admin', '789'] <class 'list'>
                line_list[0] = username
                line_list[1] = new_pwd
                # new_line = line_list[0] + '|' + line_list[1]
                # print(new_line,type(new_line))  #输出 admin|123  类型是str
                new_line = '|'.join(line_list)
                new_file.write('%s\n' % new_line)

                write_flag = True
            else:
                pass
                # new_file.write(line)
                # os.remove('db_new')
    if write_flag:
        os.rename('db', 'db.bak')
        os.rename('db_new', 'db')
        os.remove('db.bak')
        print('账号%s,密码修改成功。' % username)
    else:
        print('新密码与旧密码不能相同，请重新输入！')
        os.remove('db_new')

    return False


def main():
    t = input("1:登录：\n2：注册:\n3,修改信息：\n请输入您的操作：")
    if t == "1":
        user = input("请输入用户名：")
        pwd = input("请输入密码：")
        result = login(user, pwd)
        # print(result)
        if result:
            print("登录成功")
        else:
            print("登录失败")
    elif t == "2":
        user = input("请输入用户名：")
        pwd = input("请输入密码：")
        result = register(user, pwd)
        if result:
            print('注册成功')
        else:
            pass
    elif t == "3":
        user = input("请输入用户名：")
        pwd = input("请输入密码：")
        result = login(user, pwd)
        if result:
            r = change_pwd(user)
            # print(r)
        else:
            print("用户名密码错误，请重新输入！")


main()
