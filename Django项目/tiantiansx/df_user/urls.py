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
    # 登陆验证
    url(r'^login_existCookie/', views.login_existCookie),

]