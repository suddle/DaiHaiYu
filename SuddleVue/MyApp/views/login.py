from distributed.protocol.serialize import serializers
from django.contrib import auth
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
import json
from MyApp.models import Book
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required  # 没有登录直接访问的话，会根据settings.py中的LOGIN_URL="/login"跳转（有一个默认的）
def crm(request):
    return render(request, "userinfo.html")


def logins(request):
    response={}
    response['data'] = []
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        phone=request.POST.get("phone")
        user = authenticate(username=username, password=password,email=phone)  # 只是验证功能，还没有登录
        if user:
            login(request, user)  # 验证通过，登录
            response['code'] = 200
            response['msg'] = "success"
            return JsonResponse(response)
        else:
            print(user)  # None
            error_msg = "用户名或密码错误"
            response['code'] = 400
            response['msg'] = "fail"
            return JsonResponse(response)


def logouts(request):
    response = {}
    logout(request)
    response['code'] = 200
    response['msg'] = "success"
    return JsonResponse(response)

def regist(request):
    response = {}
    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')
        phone=request.POST.get("phone")
        User.objects.create_user(username=name, password=password,email=phone)
        response['code'] = 200
        response['msg'] = "success"
        return JsonResponse(response)