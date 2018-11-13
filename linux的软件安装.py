"""
使用rpm进行安装:
    rpm可以类比成windows下的压缩文件，他把所有相关文件打包在文件内，但要注意区别是rpm的解压是不能选择自定义目录的。
    rpm不负责文件的依赖关系的安装，只做提示。
常用参数:
    -q ： 查询软件包信息
    -qa	查询Linux系统中所有软件包
    -q 包名称	查询指定名称的软件包是否安装
    -qi 包名称	查询指定名称的软件包的详细信息
    -ql 包名称	查询指定名称软件包中的文件列表
    -qf 文件名	查询指定文件所属的软件包
    -qpi 包文件名	查询指定RPM包文件的详细信息
    -qpl 包文件名	查询指定RPM包文件的文件列表
    -i : 将包安装到系统，一般跟vh选项将安装进度显示出来
    -e : 卸载包


使用软件仓库进行安装(yum):
    修改软件仓库为镜像源
        1、备份原始仓库：
            [root@pythonDev ~]$ cp /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.bak
        2、下载阿里源进行参考信息更新到repo文件：
            [root@pythonDev ~]$ wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-6.repo
        3、下载参考数据库缓存
            [root@pythonDev ~]$ yum clean all
            [root@pythonDev ~]$ yum makecache

list	列出资源库中所有可以安装或更新的rpm包
search	搜索匹配特定字符的rpm包
install	安装软件包，会自动安装依赖关系
clean	删除缓存

使用linux安装python:             //user.qzone.qq.com/1114337841/blog/1536372167
"""