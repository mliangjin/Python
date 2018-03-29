from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register/', views.register),
    url(r'^register_dispose/', views.register_dispose),
    url(r'^login/', views.login),
]