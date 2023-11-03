from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def index(request):
    for key, value in request.GET.items():
        print(f"{key}: {value}")
    return HttpResponse("Hello, world. You're at the polls index.")
