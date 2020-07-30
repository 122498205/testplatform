from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth


# Create your views here.

def index(request):
    """登录首页"""
    if request.method == "GET":
        return render(request, "index.html")
    else:
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        print(username, password)
        if username == "" or password == "":
            return render(request, "index.html", {"error": "密码或用户名为空"})
        user = auth.authenticate(username=username, password=password)
        if user is None:
            return render(request, "index.html", {"error": "用户名或密码错误"})
        else:
            auth.login(request, user)
            return HttpResponseRedirect("/project/")


@login_required
def project_manage(request):
    return render(request, "projectmanage.html")


@login_required
def module_manage(request):
    return render(request, "modulemanage.html")



def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/index/")


