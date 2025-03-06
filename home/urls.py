from django.contrib import admin # type: ignore
from django.urls import path,include # type: ignore
from home import views

urlpatterns = [
    path("",views.index,name="home"),
    path("dashboard/",views.dashboard,name="dashboard"),
    path("about/",views.about,name="about")
]