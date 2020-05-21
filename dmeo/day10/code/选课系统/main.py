
from views import *
from services import index_dic
def main():
    show_mune()
    choose = input("请输入功能选项：")
    operate = index_dic.get(choose)
    if operate:
        func = eval(operate)
        func()
    else:
        input("输入有误，请重新输入，按任意键继续。。")
        return main()
if __name__ == '__main__':
    main()