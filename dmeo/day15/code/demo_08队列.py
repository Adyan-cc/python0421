

from queue import Queue
#1.创建队列对象
# q = Queue(maxsize=3) #3表示最多存放3个数据
#参数maxsize 是队列中允许的最大项，如果省略次参数，则无大小限制，
#返回值q是队列对象
# 2.put()方法 ， 项队列中存放数据 如果q为空，此方法阻塞，直到队列可用为止
# 3.get()方法 ，返回队列中的一个项目，如果队列为空，此方法阻塞，直到队列可用为止
# 4.get_nowait(), 不等待，直接抛出异常
# 5.full() ， 如果q已满，返回True
# 6.empty(),  如果q已空，返回True
# 7.qsize(), q中数据的个数

q = Queue(maxsize=3)
q.put("张伟强")
# print(q.empty())
q.put("刘江")
q.put("张威")
print(q.full())
# q.put("徐伟明")
print(q.get())
print(q.get())
print(q.get())
# print(q.get(timeout=3))
# print(q.get_nowait())
print(q.qsize())