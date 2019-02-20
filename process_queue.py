"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = 2019/2/19
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
from multiprocessing import Process, Queue
from threading import Thread, Lock
import time
num = 0
lock = Lock()


def fun1():
    global num
    for i in range(1000000):
        lock.acquire()
        num+=1
        lock.release()


th = Thread(target=fun1)
th.start()

th2 = Thread(target=fun1)
th2.start()
th.join()
th2.join()
print(num)


# def read(q):
#     while True:
#         # time.sleep(1)
#         print(q.get())
#
# def write(q):
#     for i in range(10):
#         q.put(i)
#
#
# if __name__ == '__main__':
#     q = Queue(5)
#     q.put(-2)
#     q.put(-1)
#     pr = Process(target=read, args=(q,))
#     pw = Process(target=write, args=(q,))
#     pr.start()
#     pw.start()
#     pr.join()
#     pw.join()

"""
进程是操作系统资源分配的基本单位，线程是任务调度和执行的基本单位。
进程之间有独立的代码和数据空间，
线程之间共享代码和数据空间。
内存分配：系统运行给进程分配不同的内存空间，而线程，除了CPU外，系统不会给线程分配内存，线程所使用的资源来源于进程
包含关系：没有进程的线程可以看做为单线程程序，一个进程中可以有多个线程同时执行
"""