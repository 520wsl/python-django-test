from django.http import HttpResponse
from django.shortcuts import render, redirect
from app01 import models


# Create your views here.
# 专门用来放函数

def login(request):
    error_msg = ""
    if request.method == "POST":  # 这里必须是大写的
        # 如果你是POST请求,我就取出提交的数据,做登录判断
        print(request.POST["email"])
        email = request.POST.get("email", None)
        pwd = request.POST.get("pwd", None)
        print(email, pwd)
        # 做是否登陆成功的判断
        if email == "1@1" and pwd == "1":
            # 登录成功
            # 回复一个特殊的响应,这个响应会让用户的浏览器请求指定的URL
            return redirect("http://www.luffycity.com")
        else:
            # 登录失败
            error_msg = "邮箱或密码错误"
    # 不是POST请求就走下面这一句
    return render(request, "login.html", {"error": error_msg})


def publisher_list(request):
    ret = models.Publisher.objects.all().order_by('id')
    return render(request, 'publisher_list.html', {"publisher_list": ret})


def add_publisher(request):
    msg = ''
    if request.method == 'POST':
        new_name = request.POST.get('publisher_name')
        if new_name:
            models.Publisher.objects.create(name=new_name)
            return redirect("/publisher_list")
        else:
            msg = '出版社名不能为空'
    return render(request, 'add_publisher.html', {'msg': msg})


def edit_publisher(request):
    msg = ''

    if request.method == "POST":
        new_name = request.POST.get("publisher_name")
        edit_id = request.POST.get("id")
        edit_publisher = models.Publisher.objects.get(id=edit_id)
        edit_publisher.name = new_name
        edit_publisher.save()
        return redirect('/publisher_list/')

    edit_id = request.GET.get('id')
    if edit_id:
        publisher_obj = models.Publisher.objects.get(id=edit_id)
        return render(request, 'edit_publisher.html', {'msg': msg, 'publisher': publisher_obj})


def delete_publisher(request):
    del_id = request.GET.get('id', None)
    if del_id:
        del_obj = models.Publisher.objects.get(id=del_id)
        del_obj.delete()
        return redirect("/publisher_list/")
    else:
        return HttpResponse('没有要删除的数据！')
