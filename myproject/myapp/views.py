# myapp/views.py
from django.http import HttpResponse
from django.shortcuts import render
import random

def index(request):
    random_number = None
    if request.method == 'POST':
        random_number = random.randint(1, 100)
    return render(request, 'index.html', {'random_number': random_number})