from django.shortcuts import render

from django.http import HttpResponse
from quicktool.models import City

# Create your views here.
# 将查询的结果可视化到网页上 quicktool/views.py文件：

def index(request):
    city = City.objects.all()
    arr = []
    for i in city:
        content = {'id':i.id,'province_id':i.province_id,'cityName':i.city_name,'description':i.description}
        arr.append(content)
    for i in arr:
        print("===type of arr.value======")
        print(type(i))
        print(i)
    print("=========")
    print(arr)
    print(type(arr))
    return HttpResponse(arr)