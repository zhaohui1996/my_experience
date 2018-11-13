"""
python中的random模块用于生成随机数，当我们需要随机产生测试数据，抽奖，验证码等等，就可以利用这个模块。
    random.random()                         用于生成一个0到1的随机浮点数: [0, 1)
    random.uniform(a,b)                     生成[a,b]或[b,a]之间的均匀分布随机浮点数。
    random.randint(a,b)                     生成[a,b]的随机整数，要求a < b。
    random.randrange(a,b)                   生成[a,b)的随机整数，第三个参数可以指定步长。
    random.choice(seq)                      从序列中随机选择一个元素，若序列为空，则抛出异常。
    random.shuffle(seqb)                    打乱源序列，源序列必须可写。
    random.sample(seq,k)                    从序列中选择k个元素返回，原序列不变。
    random.seed(n=none)                     初始化随机熵池。
random.shuffle必须跟可写的序列，同时序列被修改。如果需要保留原序列，那么就是用sample方法，第二个参数使用len来计算取样长度。
random的seed，一旦用定值初始化，则每次运行的随机现象是一致的。
"""
"""
时间模块，是开发过程中使用比较频繁的模块，比如记录日志，用户登录时间，特定时间内的数据分析等等
Python中提供了对时间日期的多种多样的处理方式，主要是在 time 和 datetime 这两个模块里。
time:
    所能表述的日期范围被限定在 1970 - 2038 之间
    time.time()	                        返回一个距Epoch的秒数，是浮点数。
    time.gmtime(seconds)	                 将秒数转化为年月日时分秒，以UTC时间为标准。
    time.localtime(seconds)	              将秒数转化为年月日时分秒，以当地时间为标准。
    time.ctime(seconds)	                 返回年月日时分秒的字符串。
    time.asctime(tuple)	                 从struct_time返回年月日时分秒字符串。
    time.mktime(tuple)	                  将struct_time转换为秒数。
    time.strftime(fmt,t)	                  按照fmt格式将struct_time显示成字符串。
    time.strptime(str,fmt)	               将年月日时分秒的字符串按照fmt解析成struct_time结构。
    
datatime:
    datetime 比 time 高级了不少，可以理解为 datetime 基于 time 进行了封装，提供了更多实用的函数。在datetime 模块中包含了几个类，具体关系如下:
        timedelta     		            主要用于计算时间跨度
        tzinfo        		            时区相关
        time          		            只关注时间
        date          		            只关注日期
        datetime  	                   同时有时间和日期
    在实际实用中，用得比较多的是 datetime.datetime 和 datetime.timedelta。
        datetime.datetime围绕一个叫做datetime.datetime对象来进行数据保存。
        
        一般使用datetime.datetime.now()获得这个实例对象。
        datetime.date()	                返回一个date对象。
        datetime.time()	                返回time对象。
        datetime.replace(n=v)	          替换字段的值后得到一个新的datetime对象。
        datetime.timetuple()	          返回time.struct_time对象。
        datetime.strftime(fmt)	          按照fmt的格式生成字符串。
        
        除了实例本身具有的方法,类本身也提供了很多好用的方法：
        datetime.today()	                  当前时间，localtime。
        datetime.now([tz])	              当前tz时区的时间。
        datetime.utcnow()	              当前UTC时间。
        datetime.fromtimestamp()	       返回时间戳的时间，有时区要求。
        datetime.strptime(str,fmt)	       按照fmt的格式解析字符串生成datetime。
timedelta:
    timedelta模块主要针对的是2个日期对象的数学运算，比如当前时间的前或后1个月，2个小时这样的需求。
    只要初始化时，指定日期参数就可以设置一个延迟时间。注意这个对象的访问只能是天和秒，需要小时等信息需要进行数学运算。
    最大的单位是天。
"""
"""
哈希散列:
    哈希算法，又叫散列算法。是一种从任何一种数据中创建小的数字“指纹”的方法。散列函数把消息或数据压缩成摘要，使得数据量变小，将数据的格式固定下来。
    如果两个散列值是不相同的（根据同一函数），那么这两个散列值的原始输入也是不相同的。
    通过散列值是恢复不出原数据的信息。
    所有安全散列算法，都在hashlib标准库里进行了管理，要使用其中的算法，首先导入hashlib库，然后使用里面的函数即可。
"""
import hashlib
test_data = b'abc123'
print(hashlib.md5(test_data).hexdigest())
#e99a18c428cb38d5f260853678922e03                                        32位
print(hashlib.sha256(test_data).hexdigest())
# 6ca13d52ca70c883e0f0bb101e425a89e8624de51db2d2392593af6a84118090       64位
"""
正规使用：
1.初始化算法库
2.使用实例化对象的update方法添加数据
3.使用实例化对象的hexdigest方法获得散列值
"""
import hashlib
a1=hashlib.md5()
a1.update(b"123")
a2=a1.hexdigest()
print(a2)


import hashlib
import os
def get_file_sha256(filename):
    if not os.path.isfile(filename):
        return""
    obj_sha256=hashlib.sha256()
    with open(filename) as fp :
        buf=fp.read(1024)
        while buf:
            obj_sha256.update(buf)
            buf=fp.read(1024)
    return obj_sha256.hexdigest()

def test_main():
    filename=""
    result=get_file_sha256(filename)
    print(result)
if __name__ == '__main__':
    test_main()