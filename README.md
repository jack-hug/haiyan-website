# haiyan-website
# flask's certificate
# second website

# 0805
rename precision

# 未解决问题 



问题：footer页面的表单需与contact页面同步，且需要封装，不能每个route都写一大段代码。

# 0819
问题：head的内容跑到body前，并且自动添加了一个符号&#65279。
解决：这是文件编码问题，在vscode里面新建一个空白html文件，然后把原内容复制进新的html里替换旧的那个。

问题：返回顶部按钮一直报错：fadeOUt() is not a function。
解决：引入了两个jquery，有了两个一样的函数名产生冲突，删除掉一个就解决了。

# 0824
问题：数据库在本地能很好运行，转到服务器就出现错误，在python shell 中操作数据库时提示：“attempt to write a readonly database”
解决：sqlite数据库文件所在的文件夹要有可读写权限，我的数据库存放在/home/precision中，所以precision要有读写权限，我的操作是使precision的所有者和所属组都改成rwx(即可读写可执行)，另外附上linux文件权限：
r(read)是4，w(write)是2，x(execute)是1。举例：如果某文件权限为7则代表可读、可写、可执行(4+2+1).若权限为6(4+2)则代表可读、可写。权限为5代表可读(4)和可执行(1).权限为3代表可写(2)和可执行(1)
sudo chmod 600 ××× （只有所有者有读和写的权限）
sudo chmod 644 ××× （所有者有读和写的权限，组用户只有读的权限）
sudo chmod 700 ××× （只有所有者有读和写以及执行的权限）
sudo chmod 666 ××× （每个人都有读和写的权限）
sudo chmod 777 ××× （每个人都有读和写以及执行的权限）

