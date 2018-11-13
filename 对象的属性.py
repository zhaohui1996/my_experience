"""
给对象添加属性
"""
def ismale(person):
	return person.sex =='男'
class Person(object):
    def __init__(self, name = None, age = None):
        self.name = name
        self.age = age
P = Person("小明", "24")
P.sex ='男'
# print(“{} 是男性吗？{}”.format(P.name, ismale(P)))
print("{} 是男性吗？{}".format(P.name, ismale(P)))

"""
给类添加属性
    给类添加属性和给对象添加属性，思路和方法都是一样的。
    不过这里要注意的是，在对象访问属性时，如果这个属性在对象空间里找不到，那么会以此查找类空间，类空间也没有的时候，继续找他的父类空间，形成一种变量查找作用域链的概念。
"""
P1 = Person("小丽", "25")
P1.sex
# AttributeError: Person instance has no attribute 'sex'
Person.sex = None #给类Person添加一个属性
P1 = Person("小丽", "25")
print(P1.sex)
# None          #如果P1这个实例对象中没有sex属性的话，那么就会访问它的类属性可以看到没有出现异常
"""
动态属性的删除
    删除的方法:
        del 对象.属性名
        delattr(对象, "属性名")
        通过以上例子可以得出一个结论：相对于动态语言，静态语言具有严谨性！所以，玩动态语言的时候，小心动态的坑！
        那么怎么避免这种情况呢？请使用__slots__
        使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的。
"""
class Person(object):
    __slots__ = ("name", "age")
P.score = 100
# AttributeError: Person instance has no attribute 'score'
"""
属性命令规则
    在python的class中，当对象绑定一个以双下划线命名的变量，称之为私有变量。其实在python中，并没有私有变量的说法，所谓的私有是人为定义的一种变量访问方式而已。
    但在python的语法中，利用了名字重整的方法来避免用户直接访问这个变量。
        xx: 公有变量
        _x: 单前置下划线,私有化属性或方法，from somemodule import *禁止导入,类对象和子类可以访问，但不希望访问到。相当于protected。
        __xx：双前置下划线,避免与子类中的属性命名冲突，无法在外部直接访问(名字重整所以访问不到)
        __xx__:双前后下划线,用户名字空间的魔法对象或属性。例如: __init__, __不要自己发明这样的名字
        xx_:单后置下划线,用于避免与Python关键词的冲突
"""
class Person:
    def __init__(self):
        self.__age = 0

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError('Expected a < 0 number')
        self.__age = value

    @age.deleter
    def age(self):
        raise AttributeError("Can't delete attribute")

p = Person()
p.age = -10



"""
元类
    道生一、一生二、二生三、三生万物
        道   即是 type
        一   即是 metaclass(元类，或者叫类生成器)
        二   即是 class(类，或者叫实例生成器)
        三   即是 instance(实例)
        万物 即是 实例的各种属性与方法，我们平常使用python时，调用的就是它们。
"""
# 创建一个Person类，拥有属性say_hello				------------------------- 二的起源
class Person():
    def __init__(self, name="人类"):
        self.name = name
    def say_hello(self):
        print('Hello, %s.' % self.name)

# 从Person类创建一个实例jim   					--------------------------- 二生三
jim = Person ('Jim')

# 使用jim调用方法say_hello   					---------------------------- 三生万物
jim.say_hello()
# 使用jim创造了比Person还多的属性  				---------------------------- 三生万物
jim.sex = '男'
"""
type
type最开始我们知道的意思是查看一个对象的类型，那么就可以理解为是谁创建了这个对象。那么
    >>> print type(1) #数值的类型
        <type 'int'>
    >>> print type("1") #字符串的类型
        <type 'str'>
    >>> print type(jim) #实例对象的类型
        <class '__main__.Person'>
    >>> print type(Person) #类的类型
        <type 'type'>
从中我们发现了，类是由type创建的。我们来看下type的申明：
    type(object_or_name, bases, dict)
    type(object) -> the object's type
    type(name, bases, dict) -> a new type
"""
def hello(self):
    print("你好{}".format(self.name))

HelloWorld = type("HiWorld", (object,), {'fn_hello': hello})

a1 = HelloWorld()
a1.name = 'Jim'
a1.fn_hello()
"""
type和类的关系
    ype可以直接生成class，但其实这中间还有一个中间体，他就称之为元类。他的名字为了区别普通类，都建议使用MetaClass作为后缀。元类相当于生成普通类的模具。
    比如我们现在有一个需求，需要生成很多类，这个类都要具备一个方法叫say_xxx，例如一个叫Student的类，就要有一个say_student方法；一个叫Doctor的类，就要有一个say_doctor的          方法；那么我们就构造一个这样规律的元类，然后通过这个元类去生成这些普通类。
    下面看一个元类：
"""
class SayMetaClass(type):
    def __new__(cls, name, bases, attrs):
        attrs['say_'+name] = lambda self,value,saying=name: print(saying+','+value+'!')
        return type.__new__(cls, name, bases, attrs)
"""
要定义一个元类，必须满足如下条件：
    元类必须由type生成，这就是道生一的概念。
    元类的操作必须在__new__中完成，同时也会传递3要素，我是谁，我从哪里来，我要到哪里去。
    如何生成刚才需求
"""
# 道生一：传入type
class SayMetaClass(type):
    # 传入三大永恒命题：类名称、父类、属性
    def __new__(cls, name, bases, attrs):
        # 创造“天赋”
        attrs['say_'+name] = lambda self,value,saying=name: print(saying+','+value+'!')
        # 传承三大永恒命题：类名称、父类、属性
        return type.__new__(cls, name, bases, attrs)
# 一生二：创建类
class Hello(object, metaclass=SayMetaClass):
    pass

# 二生三：创建实列
hello = Hello()

# 三生万物：调用实例方法
hello.say_Hello('world!')

"""
除非是要设计框架，工作中99%是不会用到元类的，学习元类的目的就是理解下python生成对象的一个过程。
"""