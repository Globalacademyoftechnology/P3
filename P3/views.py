from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Pyspiders")

def demo1(request):
    return HttpResponse("<h1>Locaion: Bangalore Basavanagudi</h1>")

def demo2(request):
    return HttpResponse("<h2>Course: Django</h2>")

def final(request):
    return render(request,"sample.html")
