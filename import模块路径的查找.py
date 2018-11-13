#常见错误:
    # ModuleNotFoundError 		: 模块没有找到的错误
    # No module named 'abab' 	: 没有abc这个模块名称
    #对象名称 ： sys.path
    #对象属性 ： 列表（list）
    # 常用方法 ： 列表中的所有常用方法，如append,insert等

#查看当前python在import时的查找路径信息
import sys
print(sys.path)
    #打印结果
    # 当前目录
    # python标准库目录
    # python标准库下的site-packages目录

    #问题解决:
        # 在导入外部模块前，把外部模块的目录添加到sys.path下
import sys
sys.path.append('/tmp')# 添加外部模块的目录

# 总结
#     当遇到模块找不到的错误时，应该先定位模块的关系：
#     ① 系统标准模块    ：	解释器的lib目录下
#     ② 第三方标准模块	：	site-packages目录下
#     ③ 工程自定义模块	：	任意位置
#     一般1，2的模块关系，错误可能是没有通过pip安装，或者在当前目录下有和他重名的文件。
#     第3个模块关系，建议在使用前，通过sys.path的insert或者append方法添加模块的绝对路径。