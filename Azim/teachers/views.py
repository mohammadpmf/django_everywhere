from django.shortcuts import render
from django.http import HttpResponse


def show_test(request):
    return HttpResponse("Test teachers")
