"""
迭代器:
	for语句的循环次数,是根据遍历序列同期中的数据个数来决定的
	在遍历过程中,可以隐式的调用了内置函数iter,被调用后,会返回一个迭代器对象.
		迭代器对象定义了__netx__方法,在每次访问时会得到一个元素,
		当没有任何元素时,__next__将通过StopIterration异常来告诉for语句停止迭代.
	x=[1,2,3]
	it=iter(x)
	print(it.__next__())	1
	print(it.__next__())	2
	print(it.__next__())	3
	print(it.__next__())	再次调用,已经没有值,返回StopIteration
        如何判断一个对象是否可以迭代
        from collections import Iterable
        isinstance([], Iterable)         # True
        isinstance(100, Iterable)       # False
    for...in实际是python语言内部实现了iter和next的调用，为使用者隐藏了迭代过程的细节。
生成器:
    利用迭代器，我们可以不断的获取数据。在实际开发中，我们有时候希望数据一开始不存放在内存上，而且在遵循某种规律的情况下，用的时候再给用户。
    在python中为我们提供生成器(generator)。他不仅具备迭代器的能力，而且他是使用时再分配，而不是事先分配空间的。
    在实际开发时，在需要迭代特性和用时获取特性时，建议使用生成器来实现，他的语法简单清晰。
    要创建一个生成器，有很多种方法。第一种方法很简单，只要把一个列表生成式的[ ] 改成( )
    L = [ x*2 for x in range(5)]
    G = ( x*2 for x in range(5))

    next(G)         # 0
    next(G)         # 2
    next(G)         # 4
    next(G)         # 6
    next(G)         # 8
    next(G)         # StopIteration

    generator非常强大。如果推算的算法比较复杂，用列表生成式的逻辑无法实现的时候，还可以用函数来实现。
    他的语法形式非常简单，就是将普通函数的return替换为yield。
    yield这里的意思不是返回，而是抛出后面的变量值，然后保存当前函数的状态，等待next的操作。
    可以看出来，当yiled在函数中使用后，这个函数已经升级为了迭代器。
    我们用函数生成器的方式改写上面的例子：
    def power2(n):
        cnt = 1
        while cnt <= n:
            yield cnt * 2




生成器与迭代器的区别:
	迭代器是所有的内容都在内存里,使用next函数来依次往下遍历.
	生成器不会把内容放在内存里,每次调用next函数时,返回的都是本次计算出来的那个元素,用完之后立刻销毁.

	总结:当整个序列占内存特别大的时候,使用生成器对象会节约内存;
		 当系统的运算资源不足时,使用迭代器对象会节约运算资源.
		 迭代器是时间优先,生成器是空间优先.

	斐波那契数列:
		斐波那契数列指的是这样一个数列：1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, …
		这个数列从第三项开始，每一项都等于前两项之和。
	def fab(max):
		n, a, b = 0, 0, 1
		while n < max:
			yield b
			# print b
			a, b = b, a + b
			n = n + 1
	更多函数访问
		https://www.ibm.com/developerworks/cn/opensource/os-cn-python-yield/index.html廖雪峰


匿名函数与可迭代函数(一般搭配起来使用)

匿名函数是以关键字lambda开始的
        lambda 参数1,参数2...:表达式
        一句话函数,不能存在return关键字
        r=lambda x,y:x+y
        print(r(2,3))


reduce函数(一个内嵌循环的函数)
    按照参数sequence中的元素顺序,来依次调用函数function,每次传入2个参数,第一个是序列中的当前参数,另一个是序列中的上一个参数在函数中的返回值.
    reduce(function,sequence,[initial])
    function:要回调的函数
    sequence:序列
    [initial]:默认值(可选)
    实现1~100的求和
        from functools import reduce
        print(reduce(lambda x,y:x+y,range(1,101)))


map函数
    按照参数sequence中的元素顺序,来依次调用函数function,得到的值会放入新的map对象中,需要通过list或者tuple转换.
    map(function,sequence[,sequence])
    function:要回调的函数
    sequence:一个或多个序列
    结果需要使用list或者tuple转化
    进行平方运算:
        t=map(lambda x:x**2,[1,2,3,4,5])
        print(list(t))
    对序列依次求和:
        t=map(lambda x,y:x+y,[1,2,3,4,5],[1,2,3,5])
        print(list(t))


filter函数
    有2个输入参数,一个是filter的处理函数,另一个是待处理的序列对象.
    运行时,filter函数会把序列对象中的元素]依次放到filter的处理函数中,如果返回True,就留下,反之就舍去.
    返回值是一个filter类型,需要将其转成列表或者元尊才可以使用
    filter(function or None,sequence)
    如果函数为None,则返回的是sequence
    过滤偶数:
        t=filter(lambda x:x%2==0,[1,2,3,4,5,6,7,,8,9,10])
        print(list(t))
每个可迭代函数返回值都属于一个生成器函数对象


"""


def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        # print b
        a, b = b, a + b
        n = n + 1
for a in fab(8):
    print(a)