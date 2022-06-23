from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_varzesh3, name='varzesh3'),
]
