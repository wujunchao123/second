from django.db import models
# from datetime import datetime
# 引入django 中的用户表
from django.contrib.auth.models import User
# Create your models here.





class UserInfo(models.Model):
    # 编号
    id = models.AutoField(primary_key=True)
    # 用户昵称
    nickname = models.CharField(max_length=255, unique=True, verbose_name="用户昵称")
    # 用户年龄
    age = models.IntegerField(default=18, verbose_name="用户年龄")
    # 用户性别
    gender = models.CharField(max_length=10, default='男', verbose_name="用户性别")
    # 用户头像
    header = models.ImageField(upload_to="static/upload/", default="/static/user/image/2.jpg", verbose_name="用户头像")
    # 联系电话
    phone = models.CharField(max_length=50, default='11111111111', verbose_name="联系方式")
    # 收货地址
    # site = models.CharField(max_length=255, verbose_name="收货地址")
    # 一对一关联用户表
    user = models.OneToOneField(User, on_delete=models.CASCADE)





