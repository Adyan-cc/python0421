### **Python** **解释器和集成环境安装**

- 解释器：就是将自然人能看懂的文本字符，转换成了计算机可以执行的二进制数据，在计算 

  机中执行得到过程的过程

- 安装python解释器
  
  - 右击管理员身份运行-->Add python3.7 to Path,自定义安装-->next-->install for all users,选择安装位置，install-->close

- 查看python 版本 ：win+R输出cmd回车,python -V    (version)
- 进入Python环境：直接在dos命令窗口输出Python
- 安装pycharm
  - 右击管理员身份运行-->next-->选择安装位置-->全部勾选-->next,install,finish
  - 破解pycharm：将jetbrains-agent.jar破解包放入pycharm的安装bin目录下，打开help-->Edit Costom VM options-->在最后一行添加-->-javaagent:D:\PyCharm 2019.3.2\bin\jetbrains-agent.jar(是自己的pycharm安装路径)，关闭重启即可
- 在pycharm中新建.py文件，选中目录-->new-->Python file

### 第一个程序

- 在E:\python0421\day1\code路径下新建demo_01第一个Python代码文本文档，打开文档，写入print("hello wrold")，保存退出，修改后缀名为.py
- 显示文件后缀名：组织-->文件夹和搜索选项-->查看-->隐藏已知文件扩展名（勾选去掉）
- 进入文件目录，按住shift，鼠标右击，在此处打开命令窗口，执行命令，python demo_01第一个Python代码.py，文件名可以用tab键补全

### 注释

- 注释的作用：对代码进行解释说明，增强代码的可读性

- 注释分类：单行注释 #，只对一行起作业，且只对#右边的内容起作用，快捷键 ctrl+/

  ​					多行注释：‘’‘ ’‘’，三个单引号或者三个双引号，(带引号是字符串)

### 标准输出 

- 标准输出，就是将信息展示到控制台窗口中 print()

- print()可以一次输出多条数据，数据之间用逗号隔开

- 默认输出数据后，会自动换行

  - end=""：添加这个参数，输出数据后，不会换行 
  - \n：表示的换行 newline 

  - \r：表示的是回车 return

### **标准输入**

- 从键盘输入信息，返回的是str字符串
- 格式：变量名=input(),可以在input()中加一些提示信息，括号中只能写一个参数
- 使用type()可以查看数据类型