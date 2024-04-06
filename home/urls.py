from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("contact/", views.contact),
    path("register/", views.register),
    path("login/", views.login),
]
