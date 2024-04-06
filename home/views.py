from telnetlib import LOGOUT
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RegistrationForm
from django.contrib import messages

from .models import Post


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .forms import UserLoginForm

# # # import thư viện httprespone
# # def index(request):
# #     response = HttpResponse()
# #     response.writelines("<h1>Welcome to Dong A university<h1/>")
# #     response.write(
# #         "<table><tr><th>ID</th><th>Họ và tên</th><th>Lớp</th></tr><tr><th>94187</th><th>Đặng QUang ĐẠt</th><th>ST21A2A</th></tr><tr><th>94188</th><th>hồ văn cường</th><th>ST21A2A</th></tr></table>"
# #     )
# #     return response


# # from django.http import HttpResponse
# # from django.template import loader


def index(request):
    return render(request, "pages/home.html")


def contact(request):
    return render(request, "pages/contact.html")


# Create your views here.
def list(request):
    Data = {"Posts": Post.objects.all().order_by("-date")}
    return render(request, "pages/home.html", Data)


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                "/"
            )  # Chuyển hướng đến trang chính sau khi đăng ký thành công
    else:  # Xử lý yêu cầu GET
        form = RegistrationForm()
    return render(request, "pages/register.html", {"form": form})


def login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, "Đăng nhập thành công")
                return redirect("home")
            else:
                messages.error(request, "Tài khoản hoặc mật khẩu không hợp lệ")
    else:
        form = UserLoginForm()
    return render(request, "pages/login.html", {"form": form})


def Logout(request):
    LOGOUT(request)
    messages.success(request, "Successfully logged out")
    return HttpResponseRedirect("/login")


# def post_detail(request, id):
#     post = Post.get_Post(id=id)
#     return render(request, "blog/post.html", {"post": post})
