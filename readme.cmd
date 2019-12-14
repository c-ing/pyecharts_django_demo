pyecharts官网文档：http://pyecharts.org/#/zh-cn/web_django?id=django-%e5%89%8d%e5%90%8e%e7%ab%af%e5%88%86%e7%a6%bb

pyecharts的加载问题：
https://blog.csdn.net/arnolan/article/details/91459831

生成到requirement文件命令：
在重新安装pip依赖时用requirement文档协助快速安装很方便，原理就是在笔记本上先生成requirement文档，让pip把虚拟环境中的依赖自动写进去，然后台式机上的新虚拟环境根据这个文档去安装依赖，命令一共2句，如下：
在旧设备上快速生成requirement.txt的安装文件（文件名可以任意）
pip freeze > requirements.txt
将项目迁移到新设备上后，在虚拟环境中安装所需要的文件
(venv)pip install -r requirement.txt
当前总结下经验，如果要迁移项目，不要迁移venv，只要把依赖生成到requirement文件，然后在新机器上根据requirement文件安装依赖即可。
