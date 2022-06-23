from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
    return HttpResponse('Say Hello :D')

def say_goodbye(request):
    return HttpResponse('Say Goodbye :D')

def say_ok(request):
    return HttpResponse('Say OK :D')

def say_im_good(request):
    return HttpResponse('Say I\'m Good :D')

def say_im_good_pk(request, pk):
    return HttpResponse(f'Say I\'m Good :D {pk}')

def say_im_good_int_pk(request, pk):
    return HttpResponse(f'Say I\'m Good :D {pk}')

def say_im_good_str_pk(request, pk):
    return HttpResponse(f'Say I\'m Good :D {pk}')



# kar nemikard in. dige baghia ro edameh nadam. hamoonja tooye urls.py behem error midad.
# def say_im_good_float_pk(request, pk):
#     return HttpResponse(f'Say I\'m Good :D {pk}')
