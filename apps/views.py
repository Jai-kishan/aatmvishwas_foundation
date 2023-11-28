from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')


def team_member(request):
    return render(request, 'team.html')


def about_us(request):
    return render(request, 'about_us.html') 


def contact_us(request):
    return render(request, 'contact_us.html') 


def blogs(request):
    return render(request, 'blog.html') 

def donate_us(request):
    return render(request, 'donate_us.html') 