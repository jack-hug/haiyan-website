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