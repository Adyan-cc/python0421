
#向控制台输出3,2,1
def out_num(num):
    """功能：。。"""
    if num==0:
        return
    print(num)
    num-=1
    out_num(num)
out_num(3)

