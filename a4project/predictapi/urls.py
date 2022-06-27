from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    #变化检测路由
    url(r'^change_detection_api/$',views.change_detection_api, name='bhjcpai'),
    #目标检测路由
    url(r'^object_detection_api/$',views.object_detection_api, name='mbjcapi'),
    # 目标提取路由
    url(r'^target_extraction_api/$',views.target_extraction_api, name='mbtqapi'),
    # 地物分类路由
    url(r'^classification_of_features_api/$',views.classification_of_features_api, name='dwflapi'),

    url(r'^ajax/$',views.ajax,name='t'),
]
