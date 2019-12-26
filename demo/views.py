from django.shortcuts import render

# Create your views here.


import json
from random import randrange

from django.http import HttpResponse
from rest_framework.views import APIView

# 只需要在顶部声明 CurrentConfig.ONLINE_HOST 即可
from pyecharts.globals import CurrentConfig
#CurrentConfig.ONLINE_HOST = "http://127.0.0.1:8000/assets/"
from pyecharts.faker import Faker
from pyecharts.charts import Bar,Scatter,Line
from pyecharts import options as opts
from django.template import loader

import pandas as pd

from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.resources import CDN

# Create your views here.
def response_as_json(data):
    json_str = json.dumps(data)
    response = HttpResponse(
        json_str,
        content_type="application/json",
    )
    response["Access-Control-Allow-Origin"] = "*"
    return response


def json_response(data, code=200):
    data = {
        "code": code,
        "msg": "success",
        "data": data,
    }
    return response_as_json(data)


def json_error(error_string="error", code=500, **kwargs):
    data = {
        "code": code,
        "msg": error_string,
        "data": {}
    }
    data.update(kwargs)
    return response_as_json(data)


JsonResponse = json_response
JsonError = json_error


def bar_base() -> Bar:
    c = (
        Bar()
        .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
        .add_yaxis("商家A", [randrange(0, 100) for _ in range(6)])
        .add_yaxis("商家B", [randrange(0, 100) for _ in range(6)])
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
        .dump_options()
    )
    return c


def scatter_base()->Scatter:
    c = (
        Scatter()
            .add_xaxis(Faker.choose())
            .add_yaxis("商家A", Faker.values())
            .set_global_opts(title_opts=opts.TitleOpts(title="Scatter-基本示例"))
            .dump_options()
    )
    print("===========scatter======")
    print(c)
    print("=========type==========")
    print(type(c))
    return c


def line_base()->Line:
    df = pd.read_csv('D:\precast_sale.csv', parse_dates=['date'], index_col='date')
    df['amount'] = round(df['amount'] / 1000, 2)
    # print(df)
    # 季节性时间序列的可视化
    df.reset_index(inplace=True)
    # Prepare data
    df['year'] = [d.year for d in df.date]
    df['month'] = [d.strftime('%m') for d in df.date]
    years = df['year'].unique()
    grouped2 = df['amount'].groupby([df['year'], df['month']]).sum().reset_index()
    print("==============")
    print(list(grouped2.loc[grouped2.year == 2015, :]['amount']))
    c = (
        Line()
        .add_xaxis(['1','2','3','4','5','6','7','8','9','10','11','12'])
        .add_yaxis("2015年",list(grouped2.loc[grouped2.year==2015,:]['amount']))
        .add_yaxis("2016年", list(grouped2.loc[grouped2.year == 2016, :]['amount']))
        .add_yaxis("2017年", list(grouped2.loc[grouped2.year == 2017, :]['amount']))
        .add_yaxis("2018年", list(grouped2.loc[grouped2.year == 2018, :]['amount']))
        .add_yaxis("2019年", list(grouped2.loc[grouped2.year == 2019, :]['amount']))
        .set_global_opts(title_opts=opts.TitleOpts(title="Line-自营销售数据"))
        #.dump_options_with_quotes()
        .dump_options()
    )

    print("===========tpye-line=======")
    print(type(c))
    return c


class ChartView(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(bar_base()))


class ScatterView(APIView):
    def get(self,request,*args,**kwargs):
        return JsonResponse(json.loads(scatter_base()))


class LineView(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(line_base()))

class IndexView(APIView):
    def get(self, request, *args, **kwargs):
       #return HttpResponse(content=open("demo/index.html").read())
       # render(request,'index.html')
        # 以下的写法和render(request,'index.html')是等价的
       # 参考文章：https://www.cnblogs.com/yang-wei/p/9997741.html
        t = loader.get_template('index.html')
        c = {"foo": "bar"}
        return HttpResponse(t.render(c,request))


def index(request):
    return render(request,'index.html')




def getWaveform(request):
    #csv_file = 'your file'
    #data = pd.read_csv(csv_file)
    TOOLS = "hover,crosshair,pan,wheel_zoom,box_zoom,reset,save,box_select"
    picture = figure(width=1200, height=400, tools=TOOLS)
    picture.line([1,2,3,4,5], [6,7,2,4,5], color='blue', alpha=0.5)
    script, div = components(picture, CDN)
    return render(request, 'waveform.html', {'script': script, 'div': div})