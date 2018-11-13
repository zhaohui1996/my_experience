"""
在Python中，所有以双下划线_ _包起来的方法，都统称为魔术方法，例如类的初始化方法 _ _ init _ _。
基本定制类：
C.__init__(self[, arg1, ...]) 		对象初始化构造器
C.__new__(self[, arg1, ...]) 		对象创建构造器
C.__del__(self) 				   对象销毁时被调用
C.__str__(self) 				   可打印的字符输出，被str化时调用，如print(obj)
C.__repr__(self) 				   交互模式下的输出内容
C.__call__(self, *args) 		    对象调用时，被执行，如p1()
"""

"""
属性操作类：
C.__getattr__(self, attr) 			获取属性；仅当属性没有找到时调用
C.__setattr__(self, attr, val) 		设置属性
C.__delattr__(self, attr) 			删除属性
注意事项：这几个属性操作很容易出现递归调用
#  错误用法
def __setattr__(self, name, value):
    self.name = value
#  正确用法
def __setattr__(self, name, value):
    self.__dict__[name] = value  # 给类中的属性名分配值
"""

"""
容器操作类：
C.__len__(self) 				   容器的数量，当调用len()时被执行
C.__getitem__(self, ind) 		    得到元素ind索引的值，p[ind]的操作
C.__setitem__(self, ind,val) 		设置元素ind索引的值
C.__delitem__(self, ind) 			删除对应ind索引的元素
"""

"""
功能类：
__iter__(self)					   产生迭代器
__enter__(self)					   with的入口代码
__exit__(self, *args)			   with语句块的退出时执行代码
参考文档
[python魔术方法1](!http://python.jobbole.com/88367/)
[python魔术方法2](!http://python.jobbole.com/87239/)
"""