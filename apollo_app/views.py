from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('index首页')

def login(request):
    return HttpResponse('这是登录界面')

def safeA(request):
    return HttpResponse('安全a级别界面')