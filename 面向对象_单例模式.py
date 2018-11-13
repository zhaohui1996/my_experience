"""
什么是__new__()方法:
新创建一个对象的时候，python解释器自动调用对象上的__new__()。该方法至少要有一个参数cls，代表需要实例化的类，由python解释器自动传入，并且必须返回通过该类新实例化出来的实例对象（还记得我们初始化方法__init__()第一个参数self代表的是该类的实例对象，而这个实例正是__new__()返回给它的）。
关键点:
    1.位置：类中，名字固定 __new__()
    2.调用时机：新建对象的时候自动调用执行
    3.作用：返回类的实例对象
    4.应用：通常我们会重写该方法，从而自定义对象的创建过程
"""
class 类名(object):
    def __new__(cls):
    #重写__new__()方法
        return object.__new__(cls)
"""
注意:
    1.__new__⾄少要有⼀个参数cls，代表要实例化的类，此参数在实例化时由Python解释器⾃动提供。
    2.__new__必须要有返回值，返回实例化出来的实例，这点在⾃⼰实现__new__时要特别注意，⼀般return⽗类	__new__出来的实例
    3.__init__有⼀个参数self，就是这个__new__返回的实例，	__init__	在	__new__的基础上可以完成⼀些其它初始化的动作，__init__不需要返回值
    4.如果创建对象时传递了⾃定义参数，且重写了__new__⽅法，则__new__也必须	"预留"该形参,用不用都无所谓,否则__init__()⽅法将⽆法获取到该参数
"""

"""
单例模式:
在程序中，有的情况下，我们只需要某个类只有一个实例就可以完成所有的功能，没有必要通过该类创建多个对象从而浪费内存空间，这样的类称为单例类。
这种创建对象的模式称为单例模式。

例如：
我们电脑上都有一个回收站，并且有且只有一个回收站就能完成所有的垃圾回收工作
"""

"""
保证通过类只能创建出一个对象:
    1.重写__new__()方法，自定义创建对象，保证只创建一次对象：只有当没有创建过对象才创建，如果已经创建就直接返回创建过的对象
    2.使用一个私有的类属性保存创建好的对象，设置为私有的可以保护类属性不被修改
"""
class Abc(object):
    __instance=None             #私有的类属性保存创建好的对象
    def __new__(cls,name,age):      #重写__new__方法保证只创建一次对象
        if not cls.__instance:
            cls.__instance=object.__new__(cls)
        return cls.__instance

"""
保证对象只初始化化一次:
    1.既然只能创建一个对象，那么初始也只能初始化一次
    2.使用一个私有的类属性 __has_init保存是否已经初始化过
    3.在初始化方法__init__()中判断是否已经初始化过，如果没有才进行初始化
"""
class Singleton(object):
    #保存创建好的对象
    __instance = None
    #是否已经初始化
    __has_init = False

    #自定义创建对象
    def __new__(cls,name,age):
        #没有创建对象才创建
        if not cls.__instance:
            #创建
            cls.__instance = object.__new__(cls)
        return cls.__instance

    """初始化属性"""
    def __init__(self,name,age):
        if not self.__has_init:
            """没有初始化才初始化"""
            self.name = name
            self.age = age
            self.__has_init = True

    def __str__(self):
        return "我的名字为%s,今年%d" % (self.name,self.age)



#创建两次对象
s1 = Singleton('小乔',16)
s2 = Singleton('大乔',17)
print(s1)
print(s2)