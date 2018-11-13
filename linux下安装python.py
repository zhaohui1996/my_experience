"""
1.安装编译所需要的库文件:
	yum groupinstall "development tools"
	也可以只安装gcc:yum install gcc
	yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel expat-devel
2.下载源码包:
	wget https://www.python.org/ftp/python/3.6.1/Python-3.6.1.tgz
	也可以在windows下面下载文件然后传进去
	找到这个压缩的文件,然后把它解压:
	tar zxvf Python-3.6.1.tgz
	然后进去解压后的文件夹
	cd Python-3.6.1
3.编译配置:(建议提前建立文件夹,makedir)
	./configure --enable-optimizations --prefix=/usr/local/python3
	make
	make install
5.添加环境变量
	vi /etc/profile
	添加 export PATH="$PATH:/usr/local/python3/bin"
6.执行让修改生效
	source /etc/profile





注意:如果出现找不到包的情况:(教程来源)
http://pazha.github.io/yum-mirrors
修改CentOS默认yum源为mirrors.aliyun.com
1.首先备份系统自带yum源配置文件/etc/yum.repos.d/CentOS-Base.repo(非必须)
	mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
2.下载ailiyun的yum源配置文件到/etc/yum.repos.d/(3选1)
	centos7:wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
	CentOS6:wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-6.repo
	CentOS5:wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-5.repo
3.运行yum makecache生成缓存
	yum makecache
4.这时候再更新系统就会看到以下mirrors.aliyun.com信息:
	yum -y update



Linux 上安装 Django(个人使用这种方式),flask也可以这种方法
http://www.runoob.com/django/django-install.html
1.安装 setuptools
	yum install python-setuptools
	然后再执行:
	yum -y install python-devel
完成之后，就可以使用 easy_install 命令安装 django
	easy_install django
之后我们在python解释器输入以下代码来验证：
[root@solar django]# python
Python 2.7.3 (default, May 15 2014, 14:49:08)
[GCC 4.8.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import django
>>> django.VERSION
(1, 6, 5, 'final', 0)
>>>





"""
