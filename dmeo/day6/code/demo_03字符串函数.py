

# string = "hello"
# print(dir(string))

# help(string.isalpha)

# print(dir(str))
# print(dir(''))


#字符串的查找
# - find 查找，返回从左第一个指定字符的索引，找不到返回-1
# - rfind 查找，返回从右第一个指定字符的索引，找不到返回-1
# - index 查找，返回从左第一个指定字符的索引，找不到报错
# - rindex 查找，返回从右第一个指定字符的索引，找不到报错
# - count 计数功能，返回自定字符在字符串当中的个数
# string = "My name is ZhangWeiqiang"
# print(string.index("a")) #4
# print(string.index("b")) #找不到会报错
# print(string.rindex("a")) #21
# print(string.find("a")) #4
# print(string.find("b")) #-1
# print(string.rfind("a")) #21
# print(string.count("a"))

# - partition 把 mystr 以 str 分割成三部分,str 前，str 自身和 str 后
# - rpartition 从右往左把 mystr 以 str 分割成三部分,str 前，str 自身和 str 后
# - splitlines 按照行分隔，返回一个包含各行作为元素的列表,按照换行符分割
# - split 按照指定的内容进行分割，maxsplit：默认将指定的所有的内容进行分割，可以指定 maxsplit 的值，
# 如果 maxsplit=1 表示只按照第一个指定内容进行分割，后面剩余的不分割
# string = "My name is ZhangWeiqiang"
#把字符串以“a”分割成三部分
# ret1 = string.partition("a")
# ret2 = string.rpartition("a")
# print(ret1)
# print(ret2)
#修改一个文件的名字demo_03.py-->demo_03副本.py
# file_name = "demo_03.py"
# file_name = input("请输入文件名：")
# ret = file_name.rpartition(".")
# # print(ret)
# new_file_name = ret[0]+"副本"+ret[1]+ret[2]
# print(new_file_name)

# content = """床前明月光，
# 疑是地上霜。
# 举头望明月，
# 低头思故乡。"""
# # print(content)
# ret = content.splitlines()
# print(ret)

# string = "My name is ZhangWeiqiang"
#将所有内容按照空格分割
# ret = string.split(" ")
# ret = string.split(" ",maxsplit=2)
# ret = string.split(" ",2)
# ret = string.split("a")
# print(ret)


# - replace** 从左到右替换指定的元素，可以指定替换的个数，默认全部替换
# -  translate 按照对应关系来替换内容 from string import maketrans
# string = "My n1me is Zh1ngWeiqi1ng"
#将所有的"1"替换成“a"
# ret = string.replace("1","a")
# ret = string.replace("1","a",1)
# ret = string.replace("Zh1ngWeiqi1ng","liujiang")
# print(ret)

# string = "My 21me is Zh12gWeiqi12g"
# #将"12"-->"an"
# str_tab = string.maketrans("12","an")
# print(string.translate(str_tab))


#练习
FirstName = """赵钱孙李，周吴郑王。
冯陈褚卫，蒋沈韩杨。
朱秦尤许，何吕施张。
孔曹严华，金魏陶姜。
戚谢邹喻，柏水窦章。
云苏潘葛，奚范彭郎。
鲁韦昌马，苗凤花方。
俞任袁柳，酆鲍史唐。
费廉岑薛，雷贺倪汤。"""

LastName = """恨桃、依秋、依波、香巧、紫萱、涵易、忆之、幻巧、水风、安寒、白亦、惜玉、碧春、怜雪、
听南、念蕾、紫夏、凌旋、芷梦、凌寒、梦竹、千凡、采波、元冬、思菱、平卉、笑柳、雪卉、南蓉、谷梦、
巧兰、绿蝶、飞荷、平安、芷荷、怀瑶、慕易、若芹、紫安、曼冬、寻巧、寄波、尔槐、以旋、初夏、依丝、
怜南、傲菡、谷蕊、笑槐、飞兰、笑卉、迎荷、元冬、痴安、妙绿、觅雪、寒安、沛凝、白容、乐蓉、映安、
依云、映冬、凡雁、梦秋、梦凡、秋巧、若云、元容、怀蕾、灵寒、天薇、翠安、乐琴、宛南、怀蕊、白风、
访波、亦凝、易绿、夜南、曼凡、亦巧、青易、冰真、白萱、友安、海之、小蕊、又琴、天风、若松、盼菡、
秋荷、香彤、语梦、惜蕊、迎彤、沛白、雁山、易蓉、雪晴、诗珊、春冬、又绿、冰绿、半梅、笑容、沛凝、
映秋、盼烟、晓凡、涵雁、问凝、冬萱、晓山、雁蓉、梦蕊、山菡、南莲、飞双、凝丝、思萱、怀梦、雨梅、
冷霜、向松、迎丝、迎梅、雅彤、香薇、以山、碧萱、寒云、向南、书雁、怀薇、思菱、忆文、翠巧、怀山、
若山、向秋、凡白、绮烟、从蕾、天曼、又亦、从安、绮彤、之玉、凡梅、依琴、沛槐、又槐、元绿、安珊、
夏之、易槐、宛亦、白翠、丹云、问寒、易文、傲易、青旋、思真、雨珍、幻丝、代梅、盼曼、妙之、半双、若翠"""
#随机5个人名
"""
string1 = FirstName.replace("，","").replace("。","").replace("\n","")
lst = LastName.split("、")

for i in range(len(lst)):
    if "\n" in lst[i]:
        lst[i] = lst[i].replace('\n','')
# print(string1)
# print(list(string1))
import random
for i in range(5):
    string1_index = random.randint(0,len(string1)-1)
    first_name = string1[string1_index]
    # print(first_name)
    # print(lst)
    last_name = lst[random.randint(0,len(lst)-1)]
    print(first_name+last_name)
"""



# 字符串的修饰
#
# - center 让字符串在指定的长度居中，如果不能居中左短右长，可以指定填充内容，默认以空格填充
# - ljust 让字符串在指定的长度左齐，可以指定填充内容，默认以空格填充
# - rjust 让字符串在指定的长度右齐，可以指定填充内容，默认以空格填充
# - zfill 将字符串填充到指定的长度，不足地方用 0 从左开始补充
# - strip 默认去除两边的空格，去除内容可以指定
# -  rstrip 默认去除右边的空格，去除内容可以指定
# -  lstrip 默认去除左边的空格，去除内容可以指定
# - format 按照顺序，将后面的参数传递给前面的大括号
# string = "hello"
# print(string)
# print(string.center(10))
# print(string.center(10,"*"))
# print(string.zfill(10))
# string = " hello "
# print(string)
# print(string.strip())
# string2 = "**hello***"
# print(string2.strip("*"))

#format
# name = "张伟强"
# age = 18
# print("我的名字叫",name,"今年",age,"岁")
# #使用位置参数填充
# print("我的名字叫{},今年{}岁。".format(name,age))
# print("我的名字叫{1},今年{0}岁。".format(age,name))

#使用关键字参数
# content = "我的名字叫{name},今年{age}岁。"
# print(content.format(age=18,name="张伟强"))

#f"字符串{name}"
# name = "张伟强"
# age = 18
# print(f"我的名字叫{name},今年{age}岁。")

# %s字符串，%d整数，%f小数，%%-->%
# name = "张伟强"
# age = 18
# height = 1.75
# print("我叫%s,今年%d岁，身高%.2fm"%(name,age,height))
# #工号 12345 第12345位入职
# #第六位入职  00006
# work_num = 6
# print("我的工号是%05d"%work_num)

#format格式化
# 格式： :[填充字符][对齐方式 <^>][宽度] < 表示向左对齐， ^表示居中对齐， >表示向右对齐
# name = "张伟强"
# age = 18
# height = 1.75
#姓名占5个字符长度，居中，年龄占5个字符长度左对齐，填充字符用#,身高年龄占5个字符长度右对齐，填充字符用*
# print("我的名字叫{:^5},今年{:#<5}岁，身高{:*>5}m。".format(name,age,height))

#精度和进制
# print("长方形的宽{:.2f}m,长{:.2f}m".format(3/2,8/3))
# 进制
# print("十进制：{}".format(10)) #十进制的10
# print("二进制：{:b}".format(10)) #二进制的10
# print("八进制：{:o}".format(10)) #八进制的10
# print("十六进制：{:x}".format(10)) #十六进制的10

# - upper 将字符串当中所有的字母转换为大写
# - lower 将字符串当中所有的字母转换为小写
# - swapcase 将字符串当中所有的字母大小写互换
# -  title 将字串符当中的单词首字母大写，单词以非字母划分
# - capitalize 只有字符串的首字母大写
# string = "hello"
# print(string.upper())
# print(string.title())



# - isalnum 判断字符串是否完全由字母或数字组成
# - isalpha 判断字符串是否完全由字母组成
# - isdigit 判断字符串是否完全由数字组成
# -  isupper 判断字符串当中的字母是否完全是大写
# -  islower 判断字符串当中的字母是否完全是小写
# -  istitle 判断字符串是否满足 title 格式
# -  isspace 判断字符串是否完全由空格组成
# - startswith 判断字符串的开头字符，也可以截取判断
# - endswith 判断字符串的结尾字符，也可以截取判断
# string = "123abc"
# print(string.isalnum())
# print(string.isdigit())
# print(string.isalpha())
# string2 = "hello world"
# print(string2.islower())

# string3 = "hello world"
# print(string3.startswith("h"))
# print(string3.endswith("d"))
# print(string3.startswith("e",1,5))
# print(string3.endswith("l",2,-1))

# 字符串编码
#
# - encode 是编码,将字符串转换成字节码。str-->byte
# - decode 是解码 ,将字节码转换成字符串。 byte-->str
# name = "张伟强"
# b_name = name.encode("utf-8")
# print(b_name)
# str_name = b_name.decode("utf-8")
# print(str_name)

#转义字符
#输出a\nb
# print("a\\nb")
# string = "jflkdsjflkjdslkfjlkdjfglkjflkgj\
# lkdsjflkdmvclkdsflkjlkdsjflkjkjfkdsjlk"
# print(string)

# content = "Weiqing's age is 18"
# print(content)

# print("a\nb")
# print(r"a\nb")
#输出a\b\c
print("a\\b\\c")
#输出a\\b\\c
print("a\\\\b\\\\c")
print(r"a\\b\\c")