from django.urls import path
from . import views

urlpatterns = [
    path('hello', views.say_hello, name='hello'),
    path('goodbye', views.say_goodbye, name='goodbye'),
    path('ok', views.say_ok, name='ok'),
    path('im_good', views.say_im_good, name='im_good'),
    path('im_good/<pk>', views.say_im_good_pk, name='im_good_pk'),
    path('im_good/<int:pk>', views.say_im_good_int_pk, name='im_good_int_pk'),
    path('im_good/<str:pk>', views.say_im_good_str_pk, name='im_good_str_pk'),
    

    
    # in payiini ha ro zadam nadash. error mideh. alaki ham dg nazanam. hamoon int va addi kafiyeh.
    # path('im_good/<bool:pk>', views.say_im_good_bool_pk, name='im_good_bool_pk'),
    # path('im_good/<float:pk>', views.say_im_good_float_pk, name='im_good_float_pk'),
]
