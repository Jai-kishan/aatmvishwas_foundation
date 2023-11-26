from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("hello dear just !")
    return render(request, 'index.html')