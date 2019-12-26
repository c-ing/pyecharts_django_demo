项目运行命令：python manage.py runserver

echarts-下钻文章：https://segmentfault.com/a/1190000006978935
pyecharts官网文档：http://pyecharts.org/#/zh-cn/web_django?id=django-%e5%89%8d%e5%90%8e%e7%ab%af%e5%88%86%e7%a6%bb

pyecharts的加载问题：
https://blog.csdn.net/arnolan/article/details/91459831

进入到当前项目目录：cd  myproject
创建虚拟环境：virtualenv venv -p python3

激活虚拟环境：
venv\Scripts\activate     # venv为创建的虚拟环境的名称
安装完后 pyCharm 重新启动


生成到requirement文件命令：
在重新安装pip依赖时用requirement文档协助快速安装很方便，原理就是在笔记本上先生成requirement文档，让pip把虚拟环境中的依赖自动写进去，然后台式机上的新虚拟环境根据这个文档去安装依赖，命令一共2句，如下：
在旧设备上快速生成requirement.txt的安装文件（文件名可以任意）
pip freeze > requirements.txt
将项目迁移到新设备上后，在虚拟环境中安装所需要的文件
(venv)pip install -r requirements.txt
当前总结下经验，如果要迁移项目，不要迁移venv，只要把依赖生成到requirement文件，然后在新机器上根据requirement文件安装依赖即可。
生成requirements.txt的第二种方式：
# 安装
pip install pipreqs
# 在当前目录生成
pipreqs . --encoding=utf8 --force


-- bokeh
https://docs.bokeh.org/en/latest/docs/installation.html
https://www.zhangshengrong.com/p/zAaOK6A9ad/
官网例子：https://docs.bokeh.org/en/latest/docs/user_guide/bokehjs.html#userguide-bokehjs
 <script type="text/javascript" src="https://cdn.pydata.org/bokeh/release/bokeh-1.4.0.min.js"></script>
<script type="text/javascript" src="https://cdn.pydata.org/bokeh/release/bokeh-widgets-1.4.0.min.js"></script>
<script type="text/javascript" src="https://cdn.pydata.org/bokeh/release/bokeh-tables-1.4.0.min.js"></script>
<script type="text/javascript" src="https://cdn.pydata.org/bokeh/release/bokeh-gl-1.4.0.min.js"></script>
<script type="text/javascript" src="https://cdn.pydata.org/bokeh/release/bokeh-api-1.4.0.min.js"></script>



https://www.jianshu.com/p/1d367c8e9128