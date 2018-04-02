from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/', views.index),
    url(r'^lists/', views.lists),
    url(r'^detail/', views.detail),
]