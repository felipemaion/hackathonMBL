from django.urls import path
from django.urls import include, re_path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    re_path(r'^manager/$', views.ManagerList.as_view(), name='manager-list'),
]