from django.urls import path, re_path
from . import views

urlpatterns = [
    path('banners/', views.BannerListAPIView.as_view())
]

# 1.注册码云账号并登录：https://gitee.com/
# 2.创建仓库(课堂截图)
# 3.本地与服务器仓库建立连接
#
"""
1）本地配置线上的账号与邮箱
>: git config --global user.name "doctor_owen"
>: git config --global user.email "doctor_owen@163.com"

2）在本地初始化仓库(git init)，并完成项目的初步搭建(项目架构)(一般都是项目负责人完成项目启动)
# 这个过程就是git的基础部分的本地操作

3）采用 https协议 或 ssh协议 与远程git仓库通信提交提交代码(一般都是项目负责人完成)
	i) https协议方式，无需配置，但是每次提交都有验证管理员账号密码
	>: git remote add origin https://gitee.com/doctor_owen/luffy.git  # 配置远程源
	>: git push -u origin master  # 提交本地仓库到远程源

	ii) ssh协议，需要配置，配置完成之后就可以正常提交代码
	>: git remote add origin git@gitee.com:doctor_owen/luffy.git  # 配置远程源
	>: git push -u origin master  # 提交本地仓库到远程源

	iii）查看源及源链接信息
	>: git remote
	>: git remote -v

	iv）删除源链接
	>: git remote remove 源名字 

"""
# 注：origin远程源的源名，可以自定义；master是分支名，是默认的主分支
