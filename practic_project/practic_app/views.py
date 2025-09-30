from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def hello(request, name, year):
    age = 2024 - year
    return HttpResponse(f"Привіт, {name}! Тобі {age} років.")

@csrf_exempt
def hello2(request):
    name = request.GET.get('name')
    age = request.GET.get('age')
    return HttpResponse(f"Hello, {name}! You are {age} years old.")

@csrf_exempt
def hello3(request):
    name = request.GET.get('name')
    age = request.GET.get('age')
    return HttpResponse(f"Hello, {name}! You are {age} years old.") 