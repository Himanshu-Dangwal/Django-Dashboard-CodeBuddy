from django.shortcuts import render, HttpResponse # type: ignore

# Create your views here.

def index(request):
    return HttpResponse("I am home page")


def dashboard(request):
    return HttpResponse("I am dashboard")

def about(request):
    return HttpResponse("This is about page")