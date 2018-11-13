"""
文件的权限:
Linux为每个文件分配了至少10个字符来限定他的权限。为了方便记忆，可以记住一个顺口溜：
	1 +                  3 +            3 +                     3 =             10
1 ： 代表文件类型 		3：所有者 		3：所属用户组 		3：其他用户

三个操作权限：读read 、 写write 、 执行execute
固定三种用户权限：所属用户(user)，所属用户组(group)，其他组用户(other)

查看权限:
    ls-l
修改权限:
    chmod  参数 文件名  //命令格式  -R 处理指定目录以及其子目录下的所有文件

    字母方式:
        chmod u+rx filename 给所属用户加上r（读）和x（可执行）权限
        chmod g-w filename  给用户组去掉w（写）权限
        chmod o=,g+w filename  其他组用户权限为空，用户组增加w权限
        chmod a=rw filename  将所有用户权限设置为rw
        参数说明：
        u代表文件所属用户,g代表文件所属用户组,o代表其他组用户
        a：All，即全部的用户，包含拥有者，所属群组以及其他用户
        +代表添加权限，-代表去掉权限，=重新分配权限（去掉权限后再添加）
        r代表读权限，w代表写权限，x代表执行权限
    数字方式:
        chmod 000 == chmod u=,g=,o=
        chmod 777 == chmod u=rwx,g=rwx,o=rwx
        chmod 640 filename   //u用户rw权限，g用户r权限，o用户无权限
修改文件所属用户和组:
    chown username filename 修改文件所属用户
    chgrp groupname filename修改文件所属用户组
    chown username.groupname filename 同时修改文件用户和所属用户组
    chown .groupname filename 只修改文件所属用户组
    chown –R username.groupname dir//递归修改dir目录下面的所有文件和目录的用户和用户组
    错误情况：（普通用户）
    注意：chown、chgrp在root用户下使用
"""