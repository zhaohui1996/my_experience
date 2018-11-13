"""
需要在D盘的test文件下放置python文件,将'.py'改为'.txt'
实现协程处理函数def change_files,在其内部使用循环,遍历所有文件,当发现扩展名是'py'的文件后,调用os的rename方法修改扩展名:
"""
import os#导入系统模块
import asyncio#协程处理的模块


async def change_files(x):  # 协程处理函数
    files = os.listdir("D:/test")  # 列出当前目录下所有的文件

    for filename in files:          #遍历列表中的文件名
        portion = os.path.splitext(filename)  # 分离文件名字和后缀
        print(portion)

        if portion[1] == ".py":  # 根据后缀来修改,如无后缀则空
            newname = portion[0] + ".txt"  # 要改的新后缀
            os.chdir("D:/test")  # 切换文件路径,如无路径则要新建或者路径同上,做好备份
            os.rename(filename, newname)

    return '{}任务完成'.format(x)


def callback(future):  # 回调函数
    print('Callback: ', future.result())  # 返回任务结果


coroutine = change_files("修改扩展名")  # 定义协程，并传入任务
loop = asyncio.get_event_loop()  # 获得事件循环对象
task = asyncio.ensure_future(coroutine)  # 获得任务对象（对协程的封装）
task.add_done_callback(callback)  # 封装好后的协程对象（任务）就可以绑定回调函数了
loop.run_until_complete(task)  # 执行协程任务