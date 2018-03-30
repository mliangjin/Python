from django.conf.urls import url
from . import views

urlpatterns = [
    # 注册
    url(r'^register/', views.register),
    url(r'^register_dispose/', views.register_dispose),
    # 注册验证
    url(r'^register_exist/', views.register_exist),
    # 登陆
    url(r'^login/', views.login),
    url(r'^login_dispose/', views.login_dispose),
    # 用户中心
    url(r'info/', views.info),
    # 订单
    url(r'order/', views.order),
    # 地址
    url(r'site/', views.site),
    url(r'site_dispose/', views.site_dispose),

]