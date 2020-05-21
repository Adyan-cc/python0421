

# #打开文件
# file = open("demo_02/1.txt",mode="r")
#读取文件
# ret = file.read()
# print(ret)
# file.write("python") #读的模式打开无法进行写操作
#关闭文件
# file.close()
# file叫做文件句柄(变量)，用来操作文件
#第一个参数是文件的路径
#第二个参数 mode=访问文件的模型，r表示读，默认是r模式



# # 2.写文件 write
# file = open("demo_02/2.txt",mode="w")
# file.write("hello world")
# file.close()
# #文件不存在，会自动创建文件(不会创建目录)


# rb 以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。一般用于 非文本文件如图片等。
#  注意：二进制文件把内容表示为一个特殊的 bytes 字符串类型。

# file = open("demo/1.png","rb")
# file = open("demo_02/1.txt","rb")
# ret = file.read()
# print(ret)

# r+ 打开一个文件用于读写。文件指针将会放在文件的开头。
# file = open("demo_02/1.txt","r+")
# file.write("zhang wei qiang")
# file.close()



# wb 以二进制格式打开一个文件只用于写入。
# 如果该文件已存在则打开文件，并从开 头开始编辑，即原有内容会被删除。
# 如果该文件不存在，创建新文件。一般用于 非文本文件如图片等。

# #写入一张图片
# from demo.img import img2
# file = open("demo_02/1.jpg","wb")
# file.write(img2)
# file.close()


# w+ 打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，
# 即 原有内容会被删除。如果该文件不存在，创建新文件。
# file = open("demo_02/1.txt","w+")
# ret = file.read()
# print(ret)
# file.close()


# a 打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。
# 也 就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件 进行写入。

#在demo_02下的2.txt中追加“python”
# file = open("demo_02/2.txt","a")
# file.write("python")
# file.close()

# a+  打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。
# 文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
file = open("demo_02/2.txt","a+")
ret = file.read()
print(ret)
file.close()