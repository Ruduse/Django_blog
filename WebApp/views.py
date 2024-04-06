# Create your views here.
from django.shortcuts import get_object_or_404, render
from .models import Post


# Create your views here.
def list(request):
    Data = {"Posts": Post.objects.all().order_by("-dateTime")}
    return render(request, "blog/blog.html", Data)


def post_detail(request, id):
    post = Post.get_Post(id=id)
    return render(request, "blog/post.html", {"post": post})


from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from WebApp.form import BlogPostForm
from .models import *


@login_required(login_url="/login")
def add_blogs(request):
    if request.method == "POST":
        form = BlogPostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            blogpost = form.save(commit=False)
            blogpost.author = request.user
            blogpost.save()
            obj = form.instance
            alert = True
            return render(
                request, "pages/add_blogs.html/", {"obj": obj, "alert": alert}
            )
    else:
        form = BlogPostForm()
        return render(request, "pages/add_blogs.html/", {"form": form})
