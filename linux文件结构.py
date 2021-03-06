"""
Linux和Window下“我的电脑”的区别:
    Window下整个磁盘，被分为了C盘、D盘、E盘……
    Linux系统则是用/根目录来管理所有盘符的，是一种典型的树形结构。
Linux有个基本思想：一切皆文件(正如在python中,一切皆对象一样)

/bin 存放二进制可执行文件（命令），所有用户都可以使用
/sbin 存放二进制可执行文件，只有root用户可以使用
/boot 系统启动需要的核心文件
/dev  设备目录
/home 用户的主目录
/lib  系统共享动态链接库
/mnt  挂载目录，通常挂载到该目录下
/etc 存放系统配置文件目录
/etc/passswd 用户信息文件
/etc/group 用户组信息文件
/var 用来存放经常变动的文件。比如缓存、登录文件，mysql数据库文件等
/tmp  临时目录，用来存放临时文件
/proc 虚拟目录，是内存的映射，可以访问到内存中的系统信息
/sys 和proc类似，存放和内核相关的信息和数据
/root root用户的主目录
/usr 存放应用程序和文件（类似于windows的system32、program files目录）
/usr/bin、/usr/sbin：这是对/bin、/sbin的一个补充

常用目录操作:
cd	    切换到当前用户的主目录(/home/用户目录)，用户登陆的时候，默认的目录就是用户的主目录。
cd ~	同上
cd /	进入根目录
cd ..	切换到上级目录
cd -	进入上次所在目录

相对路径与绝对路径:
    区别，就是看是否有最顶层的目录来标识他。
    在Linux下，只要不是从/根下标记的文件，都称之为相对标识。
    绝对路径的好处是，一定准确的找到这个文件。缺点是表示一个文件要写过多的字符串。
    相对路径正好相反，用较少的字符来找到文件，但准确性需要提前考虑好。

如何修改PATH路径:
临时:
    export PATH=$PATH:新加的查找路径
永久:
    修改/ect/profile文件，对所有用户都生效
    修改家目录下的.bashrc文件，对当前用户生效
"""