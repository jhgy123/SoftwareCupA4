from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    # 首页路由
    url(r'^index/$', views.index, name="index"),
    url(r'^about/$',views.bhjc, name="about"),
    # 变化检测路由
    url(r'^bhjc/$',views.about, name="bhjc"),
    # 地物分类路由
    url(r'^dwfl/$', views.dwfl, name="dwfl"),
    # 目标检测路由
    url(r'^mbjc/$', views.mbjc, name="mbjc"),
    # 目标提取路由
    url(r'^mbtq/$', views.mbtq, name="mbtq"),



    url(r'^upload/$',views.upload),
    url(r'^ajaxtest/$',views.ajaxtest),
    url(r'^predicttest/$', views.predicttest),


]