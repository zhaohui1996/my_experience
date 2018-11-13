# 装饰器实际是软件设计模式的一种名称，他要求具备的功能是：
# 是一个可调用的对象（a callable object）
# 在不改变原函数代码的基础上，增加新的功能

# 使用场景:
#     场景一：（运维和测试上）
    #     在原有功能基础上，增加日志记录；
    #     性能测试，比如查看某个功能的执行时间，寻找最优的解决方案；
#     场景二：（开发中）
    #     判断功能调用时，参数的合法性；
    #     调用功能前，身份权限的验证；
    #     框架代码和用户代码的衔接，比如通用功能上预留自定义功能的组合；


# 函数名就是一个可调用对象的别名
def fun():
	print("in fun...")
# 相当于定义了一个名字空间：{'fun': <function>}
# 既然fun是一个名称，那就可以像普通变量一样，传递或重指向。
# 函数名可以赋值，也可以被重命名
def fun():
    print('我是老函数')

def factory(old_fun):
    print('='*20)
    old_fun()
    print('='*20)

factory(fun)
    # old_name = factory(old_name)这句话就是生成装饰器的核心语句。为了避免每次都写这样的无脑代码，python提供了一个便捷的写法，我们称之为语法糖。
    # 语法糖的写法：
    # · 找到要装饰的函数
    # · 在上面写上@，然后跟装饰器函数的名称
# @decortate
# def fun():
# 	print('in fun() ...')


# 无参数装饰器
# 增加函数什么时候运行的功能
import time#导入时间模块
        #time.time（）：获取当前的秒数（计算机）
        #Time.ctime():获取当前时间的字符串
def time_fun(func):
    def my_time():
        print(f"{func.__name__} running at {time.ctime()}")
        func()
    return my_time

@time_fun
def fun1():
    print("+++++++++")

fun1()
time.sleep(2)
fun1()

# 被装饰函数有参数
# 装饰器的核心是内部函数的行为被重命名；
# 内部函数的形式要满足原函数形式；
import time

def time_fun(func):
    def my_time(arg1):						# 内部函数里预留接口
        print(f"{func.__name__} running at {time.ctime()}")
        func(arg1)							# 原函数传递参数
    return my_time

@time_fun
def fun1(arg1):
    print("+++++{}++++".format(arg1))

fun1(10)
time.sleep(2)
fun1(10)


# 被装饰函数有不定参数和返回值
# 原函数有返回值，内部装饰函数也接收返回值进行返回。
import time

def time_fun(func):
    def my_time(*args, **kwargs):
        print(f"{func.__name__} running at {time.ctime()}")
        func(*args, **kwargs)
    return my_time

@time_fun
def fun1(arg1, arg2, name):
    print("+++++{},{},{}++++".format(arg1, arg2, name))

fun1(10, 20, name='rocky')
time.sleep(2)
fun1(10, 20, name='jim')

#改变装饰器行为
# 在装饰器中，我们也有一种需求，根据传入的参数不同，装饰的行为方式也会不同，那么如何定义这种装饰器那。
import time

def time_fun(flags):
    def time_arg(func):
        def my_time(*args, **kwargs):
            print(f"{func.__name__} running at {time.ctime()}")
            print("the flags is {}".format(flags))
            return func(*args, **kwargs)
        return my_time
    return time_arg

@time_fun("itsource")
def fun1(arg1, arg2, name):
    print("+++++{},{},{}++++".format(arg1, arg2, name))

fun1(10, 20, name='rocky')
time.sleep(2)
fun1(10, 20, name='jim')


# 用类来定义装饰器
# 具有__call__方法的对象空间，就称之为可执行对象，每定义一个函数，就相当于在空间中定义了__call__方法。
# Test的__init__方法应该接收被装饰函数的名称
# 调用fun()实际就是调用了Test类的__call__方法
class Test():
    def __init__(self, fn):
        self.old_fun = fn

    def __call__(self,):
        # 装饰内容
        ret = self.old_fun()

@Test
def fun():
    pass
fun()


# 多层装饰
# 在实际开发时，一个原函数，可以使用多个装饰函数进行修饰，这种行为就称之为多层装饰。
# 对于多层装饰，要理解他的执行过程
def bold(fn):
    def wrapper():
        return f'<b>{fn()}</b>'
    return wrapper


def italic(fn):
    def wrapper():
        return f'<i>{fn()}</i>'
    return wrapper


@italic
@bold
def hello():
    return 'Hello World'


print(hello())


# 闭包函数
    # 闭包，实际是一个特殊的函数，他的特点是：
        # 一个函数A里定义了另外一个函数B；
        # 函数B里使用了函数A作用域里的标识符；
        # 函数B给外部使用；
    # 原理
# __closure__属性：
    # 	普通函数：None
    # 	闭包：	元组，数量等于引用外部函数作用域的标识符
# cell_contents：
    # 	闭包__closure__里保存的cell元素的属性
    # 	保存了引用外部函数作用域标识符
    # 定义:
    #     在外部函数A里定义一个内部函数B
    #     内部函数B里使用了外部函数A的作用域变量
    #     外部函数A返回了内部函数B的名字
def count1():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs

f1, f2, f3 = count1()

print(f1())
print(f2())
print(f3())

# 延迟执行、惰性函数
# # # 由于使用的是代码段返回的方式，换句话，就是这个功能的执行是被延迟执行的。那这个闭包有时又称之为惰性函数。
# # # 比如我有一个非常耗时的计算操作，在系统初始化的时候，如果执行了，那么会影响系统的启动速度，这个时候，就可以使用闭包的惰性特性，来规避这样的问题。
def lazy_sum(*args):
    def mysum():
        count = 0
        for i in args:
            count += i
        return count
    return mysum

a = lazy_sum(*(range(101)))
print(a)
print(a())

# 保持一个状态稍后使用，装饰器的核心
def lazy_sum(arg):
    def mysum():
        count = 0
        for i in arg:
            count += i
        return count
    return mysum


buf = [1, 2, 3, 4]
a = lazy_sum(buf)
buf.append(20)
print(a)
print(a())