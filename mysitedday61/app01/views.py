from django.shortcuts import render, redirect


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

def user_list(request):
    pass