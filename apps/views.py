from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("hello dear just !")
    # return render(request, 'new_index.html')
    return render(request, 'index.html')


def team_member(request):
    return render(request, 'team.html')


def about_us(request):
    return render(request, 'about_us.html') 