from django.contrib import admin # type: ignore
from django.urls import path,include # type: ignore
from auth import views

urlpatterns = [
    path("login/",views.login,name="login"),
    path("register/",views.register,name="register"),
]