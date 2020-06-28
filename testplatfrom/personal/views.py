from django.shortcuts import render

# Create your views here.

def index(request):
    """登录首页"""
    if request.method =="GET":
        return render(request,"index.html")
    else:
        username = request.GET.get("username", "")
        password = request.GET.get("password", "")
        print(username, password)
        if username == "" or password == "":
            return render(request, "index.html", {"error": "密码或用户名为空"})


def login_action(request):
    """处理登录请求 """
