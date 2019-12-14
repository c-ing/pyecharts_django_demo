from django.conf.urls import url
from . import views

urlpatterns = {
    url(r'bar/$',views.ChartView.as_view(),name='demo'),
    url(r'scatter/$',views.ScatterView.as_view(),name='demo'),
    url(r'line/$',views.LineView.as_view(),name='demo'),
    url(r'^index/$', views.IndexView.as_view(), name='demo'),
    #url(r'^index/$', views.index, name='demo'),
    url(r'^waveform/$', views.getWaveform, name='demo'),
}
