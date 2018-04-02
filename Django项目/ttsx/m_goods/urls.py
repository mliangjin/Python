from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/', views.index),
    url(r'^list(\d+)_(\d+)_(\d+)/', views.lists),
    url(r'^(\d+)/', views.detail),
]