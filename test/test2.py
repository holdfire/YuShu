# 第6章：进程和线程
# 6.1 什么是进程 process
# 进程是竞争计算机资源的基本单位
# 单核CPU，在某一时刻只能够执行一个应用程序
# 但可以在不同的应用程序之间切换
# 进程调度：

# 6.2 什么是线程 thread
# 线程是进程的一部分
# 进程是用来分配资源的，如内存资源
# 线程则是 利用CPU执行代码

# 6.3 多线程的好处
# 线程属于进程，访问进程的资源
# 线程之间的前切换所消耗的资源要比进程切换消耗的资源要小。
# 多核能够并行地执行程序

# 6.5 全局解释器GIL
# python不能充分利用多核CPU的优势，是因为python有GIL:global interpreter lock
# 锁：为了保证线程安全
# 细粒度锁：程序员主动加锁
# 粗粒度锁：解释器GIL，多核CPU，只有一个线程执行，一定程度上保证线程安全
# 可行的解决思路：使用多进程，但进程通信比较复杂

# 6.6 对于IO密集型程序，多线程是有意义的
# 对于CPU密集型程序（非常严重依赖CPU计算），python多线程意义不大
# 对于IO密集型程序（如查询数据库，请求网络资源，读写文件）
# IO密集型程序，CPU有很长时间在等待，

# 6.7 flask多线程
# flask是一个web框架
# 区分webserver(nginx, apache)， web框架(flask, )



import threading
import time


def worker():
    print('I am a thread')
    t = threading.current_thread()
    time.sleep(10)
    print(t.getName())

t = threading.current_thread()
print(t.getName())

new_t = threading.Thread(target=worker, name = 'threadxxxx')
new_t.start()
