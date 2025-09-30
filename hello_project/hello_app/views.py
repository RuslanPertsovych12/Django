from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def hello_name(request, name):
    return HttpResponse(f"Hello, {name}!")

# views.py
from django.http import HttpResponse

letter_dict = {
    "A": "00",
    "C": "01",
    "G": "10",
    "T": "11",
}

def letters_view(request, letters):
    binary_str = "".join(letter_dict.get(letter.upper(), "??") for letter in letters)
    if "??" in binary_str:
        return HttpResponse("Помилка: невідомі літери у рядку")
    number = int(binary_str, 2)
    return HttpResponse(f"Бінарний рядок: {binary_str}, як число: {number}")
