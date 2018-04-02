from django.conf.urls import url
from . import views

urlpatterns = [
    # 注册
    url(r'^register/', views.register),
    url(r'^register_dispose/', views.register_dispose),
    # 登陆
    url(r'^login/', views.login),
    # 信息
    url(r'^info/', views.info),
    # 订单
    url(r'^order/', views.order),
    # 地址
    url(r'^site/', views.site),
    # 退出
    url(r'^logout/', views.logout),
]