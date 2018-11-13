"""
添:
useradd 用户名                添加一个用户
    参数-g 组id
        -d 用户主目录
        -u 用户id
示例：useradd -g 501 -d /lisi -u 502 lisi
改:
usermod
参数-g 组id
    -d 用户主目录
    -u 用户id
    -l 修改用户名
示例：usermodel -g 501 -d /lisi -u 502 lisi
删:
userdel
userdel  -r  用户名    	//删除用户信息同时用户对应主目录也被删除

组的操作:
添加组:
    groupadd  组名            //添加一个用户组
    groupadd -g 组id 组名    //添加组的同时指定组id
修改组:
    groupmod
    groupmod -n 新组名 旧组名    //修改组名称
    groupmod -g 组id 组名       //修改组id
删除组:
    groupdel 组名  //删除用户组（组里有用户，不能删除）
修改密码:
    passwd        //修改自己的密码
    passwd 用户名 //修改指定用户的密码，仅root用户可以使用
"""