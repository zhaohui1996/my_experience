"""
进程---应用程序的执行实例(相当于windows运行的exe文件)
线程---执行进程中的路径,线程是进程的一部分

线程主抓中央处理器执行代码的过程,其余的资源的保护和管理由进程去完成.

一个进程可以有一个或者多个线程组成

线程是CPU调度的最小单位,进程是CPU资源分配的最小单位
操作系统通过线程与进程,可以将资源分配和调度分开,以实现更合理地使用CPU运算资源

"""
#当一个进程只有一个线程时,叫做单线程,超过一个线程就叫多线程
#主线程   子线程
"""
查看当前线程的实例
"""
import threading
print(threading.current_thread())
"""
threading.enumerate:返回一个正在运行线程的list
threading.activeCount:返回正在运行的线程数量   相当于是len(threading.enumerate())
主线程:MainThread

创建子线程的两种方法:
    类threading.Thread的实例化,然后调用对象的start方法
    派生threading.Thread,实例化新类,并调用start方法
"""
import threading
#定义一个线程处理的函数
def handle(sid):
    #打印出当前线程的参数及其名称
    print(f"Thread {sid} run",threading.current_thread())
#使用循环创建多个线程
for i in range(1,11):
    t = threading.Thread(target=handle,args=(i,))#将i作为参数传入线程中
    #启动线程
    t.start()

print("主线程:",threading.current_thread())#打印主线程的信息