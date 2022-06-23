from django.urls import path
from varzesh3 import views

urlpatterns = [
    path('', views.show_varzesh3, name='varzesh3'),
]
