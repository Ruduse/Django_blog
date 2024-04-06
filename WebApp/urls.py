from django.urls import path
from django.contrib import admin
from WebApp.models import Post
from mysite import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path("", views.list),
    path("add_blogs/", views.add_blogs),
    path("<int:id>", views.post_detail),
]

# views.post_detail, name="post_detail",
