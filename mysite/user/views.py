from io import BytesIO

from django.http import HttpResponse


from django.shortcuts import render
# 引入数据库用户名表
from django.contrib.auth.models import User
# django内置的登陆推出方法
from django.contrib.auth import authenticate, logout, login
# 引入models模块
from . import models
# 引入验证码模块
from . import utils

import math
from django.shortcuts import redirect


# 验证码
def code(request):
    img, code = utils.create_code()
    # 将验证码保存到code中
    request.session['code'] = code
    file = BytesIO()
    img.save(file, 'PNG')
    return HttpResponse(file.getvalue())


# 用户登陆
def user_login(request):
    if request.method == "GET":
        return render(request, "user/login.html", {"msg": "请登录"})
    elif request.method == "POST":
        username = request.POST["username"].strip()
        password = request.POST["password"].strip()
        # 验证码
        # code = request.POST['code']
        # mycode = request.session['code']
        # if code.upper() != mycode.upper():
        #     return render(request, 'user/login.html', {'msg': '验证码输入错误'})
        # del request.session['code']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                # 将验证通过的用户信息保存到reques，
                login(request, user)
                request.session['login'] = user.id

                return render(request, "user/userInfo.html", {"user":request.user, "img": request.user.userinfo.header})
            else:
                return render(request, "user/login.html", {"error_code": 2, "msg": "你的账号已经被锁定，请联系管理员"})
        else:
            return render(request, "user/login.html", {"error_code": 3, "msg": "用户名称或者密码错误，请重新登录"})


# 用户注册
def register(request):
    if request.method == "GET":
        return render(request, "user/register.html", {"msg": "请认真填写如下选项"})
    elif request.method == "POST":
        username = request.POST["username"].strip()
        password = request.POST["password"].strip()
        nickname = request.POST["nickname"]
        confirmpwd = request.POST["confirmpwd"].strip()
        phone = request.POST["phone"]

        # 两次密码判断
        if password != confirmpwd:
            return render(request, 'user/register.html', {"error_code": 1, "msg": "两次密码不一致，请重新输入"})

        # 验证码判断
        # code = request.POST['code']
        # mycode = request.session['code']
        # if code.upper() != mycode.upper():
        #     return render(request, 'user/register.html', {'msg': '验证码输入错误'})
        # del request.session['code']

        # 判断用户名是否相可用
        if len(username) < 1:
            return render(request, "user/register.html", {"msg": "用户名不能为空！！！"})
        if len(password) < 6:
            return render(request, "user/register.html", {"msg": "密码长度不能小于6位！！！"})
        if len(phone) != 11:
            return render(request, 'user/register.html', {'msg':'手机号输入错误！！'})

        try:
            User.objects.get(username=username)
            return render(request, 'user/register.html', {"error_code": 2, "msg": "用户名已存在，请重新输入"})
        except:
            try:
                models.UserInfo.object.get(nickname=nickname)
                return render(request, "user/register.html", {"error_code": 3, "msg": "该用户昵称已经存在，请重新输入"})
            except:
                # 保存用户信息
                user = User.objects.create_user(username=username, password=password,)
                userInfo = models.UserInfo(nickname=nickname,phone=phone, user=user)

                user.save()
                userInfo.save()

                return render(request, "user/login.html", {"error_code": 1, "msg": "用户注册成功，请登录"})


# 用户退出
def user_logout(request):
    logout(request)
    return render(request, "user/login.html", {"error_code": 4, "msg": "退出成功，请重新登录"})


# 用户修改
def update(request):
    user = request.user
    if request.method == "GET":
        # user = models.User.objects.get(id=request.session['login'])
        return render(request, "user/update.html", {"user": user})
    elif request.method == 'POST':

        age = request.POST['age']
        phone = request.POST['phone']
        nickname = request.POST['nickname']
        # 获取文件域对象
        header = request.FILES.get('header')
        print(header)
        id = request.session['login']

        user.userinfo.phone = phone
        user.userinfo.age = age
        user.userinfo.nickname = nickname
        user.userinfo.header = header
        user.userinfo.save()
        return render(request, 'user/userInfo.html', {"msg": "修改成功!!", 'user': request.user,
                                                      "img": request.user.userinfo.header})


# 展示用户信息
def user_info(request):
    if request.method == "GET":
        return render(request, "user/userInfo.html", {"img": request.user.userinfo.header})
    if request.method == "POST":
        return render(request, "user/userInfo.html", {})

# 删除用户
# def delete_user(request):
# #     u_id = request.GET["id"]
# #     user = models.User.objects.get(pk=u_id)
# #     user.delete()
# #     return HttpResponse(<h2>删除成功</h2>)

# django 封装文件上传
def register2(request):
    if request.method == 'GET':
        return render(request, 'user/userInfo.html', {'msg':'请按照格式进行修改'})
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        nickname = request.POST['nickname']
        # 获取文件域对象
        header = request.FILES['header']
        print(header)
        user = models.User(username=username,
                           password=password,
                           nickname=nickname,
                           header=header)
        user.save()
        return render(request, 'user/userInfo.html',
                      {"msg": "修改成功!!", 'user': user})


# 修改密码
def update_pw(request):
    # 获取当前用户
    user = request.user
    if request.method == "GET":
        return render(request, "user/update_pw.html", {"msg": "请正确修改信息！！", "user": user})
    elif request.method == "POST":
        opassword = request.POST["opassword"].strip()
        npassword = request.POST["npassword"].strip()
        confirmpwd = request.POST["confirmpwd"]

        # 验证码判断
        # code = request.POST['code']
        # mycode = request.session['code']
        # if code.upper() != mycode.upper():
        #     return render(request, 'user/register.html', {'msg': '验证码输入错误'})
        # del request.session['code']

        user = authenticate(username=request.user.username, password=opassword)
        if user is not None:
            if npassword != confirmpwd:
                return render(request, "user/update_pw.html", {"msg": "两次输入密码不一致，请重新输入！！"})
            else:
                user.set_password(npassword)
                user.save()
                logout(request)
                return render(request, "user/login.html", {"msg": "修改成功，请重新登录..."})
        else:
            return render(request, "user/update_pw.html", {"error_code": 2, "msg": "原密码输入错误请重新输入"})
