from django.shortcuts import render
# 引入数据库用户名表
from django.contrib.auth.models import User
# django内置的登陆推出方法
from django.contrib.auth import authenticate,logout,login
# 引入models模块
from . import models
from django.shortcuts import redirect


# 用户登陆
def user_login(request):
    if request.method == "GET":
        return render(request, "user/login.html", {"msg": "请登录"})
    elif request.method == "POST":
        username = request.POST["username"].strip()
        password = request.POST["password"].strip()

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                # 将验证通过的用户信息保存到reques，
                login(request, user)
                request.session['login'] = user.id

                return render(request, "user/userInfo.html", {"user": user})
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
        # phone = request.POST["phone"]

        # 两次密码判断
        if password != confirmpwd:
            return render(request, 'user/register.html', {"error_code": 1, "msg": "两次密码不一致，请重新输入"})

        # 验证码判断

        # 判断用户名是否相可用
        if len(username) < 1:
            return render(request, "user/register.html", {"msg": "用户名不能为空！！！"})
        if len(password) < 6:
            return render(request, "user/register.html", {"msg": "密码长度不能小于6位！！！"})

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
                userInfo = models.UserInfo(nickname=nickname, user=user)

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
        # id = request.session['login']
        #
        # user = models.User.objects.get(id=id)
        # user = models.User(phone=phone,
        #                    age=age,
        #                    nickname=nickname,
        #                    header=header)
        user.userinfo.phone = phone
        user.userinfo.age = age
        user.userinfo.nickname = nickname
        user.userinfo.header = header
        user.userinfo.save()
        return render(request, 'user/userInfo.html',
                      {"msg": "修改成功!!", 'user': user})



        # nickname = request.POST["nickname"]
        # age = request.POST['age']
        # # 获取用户
        # # user = models.User.objects.get(id=request.session['login'])
        # user = models.User.objects.get(id=request.user)
        # # 修改值
        # user.age = age
        # user.nickname = nickname
        # # 保存
        # user.save()
        #
        # return redirect('/user/')

# 展示用户信息
def user_info(request):
    if request.method == "GET":
        return render(request, "user/userInfo.html", {})
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
        return render(request,'user/userInfo.html',{'msg':'请按照格式进行修改'})
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
        return render(request,'user/userInfo.html',
                      {"msg": "修改成功!!", 'user':user})