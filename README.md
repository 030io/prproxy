PRProxy : python reverse proxy
====================

##只测试了一个运行环境

*	系统: Linux  
*	python版本: 3.4  
*	第三方模块: tornado, chardet  

**源码很简单,代码很少,想移植到python2.7改几行代码就可以了**

##安装运行:

1.	git clone https://github.com/030io/prproxy  
2.	cd prproxy&python3 setup.py install  
3.	cp -r example/  myprproxy/   
4.  vim ./myprproxy/config  
5. 	python3 start.py  

---------------------

##功能: python实现的一个很简单的反向代理

*	反向代理,可以自设域名  
*	可以替换html源码中的域名  
*	屏蔽指定后缀, 屏蔽某些特殊文件, 如:mp4,flv等体积很大的文件  

###未实现功能:

*	反向代理二级域名,如 反向代理*.example.com  可以把xxx.yourdomain.com反向代理到xxx.example.com  

-------------------------

##适用的地方:

*	翻墙  
*	镜像网站  
*	黑帽seo  

------------------------

##使用MIT开源协议
