from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request,"web/index.html")
def research(request):
    return render(request,"web/research.html")
def project(request):
    return render(request,"web/project.html")
def skill(request):
    return render(request,"web/skill.html")
def course(request):
    return render(request,"web/course.html")
def award(request):
    return render(request,"web/award.html")
def switch(request):
    return render(request,"web/switch.html")
# Create your views here.
