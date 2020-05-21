
import tkinter as tk
top = tk.Tk()# 创建主窗口
top.title("坦克1.2.0")# 主窗口标题
top.geometry('700x700')# 设置主窗口大小
lab = tk.Label(top, text='') # 添加标签
lab.pack()
btn = tk.Button(top)# 添加按钮
btn.pack()
btn['text'] = "这是按钮"# 给btn按钮text属性赋值
def click(): # 定义事件函数
    lab['text'] = "那是谁呀，按了按钮就没下文了？"
btn['command'] = click # 给btn按钮绑定事件
top.mainloop()
second = tk.Toplevel(top)
second.title("副窗口")
sublab = tk.Label(second)
sublab.pack()
sublab['text'] = "这是一个在副窗口中的标签。"