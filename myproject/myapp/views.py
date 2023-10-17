from django.shortcuts import render
from django.http import HttpResponse
import random 
import string

# Create your views here.
def index(request):
    return render(request, 'index.html', {'password': None})

def es_mx(request):
    return render(request, 'es-mx.html', {'password': None})

def generate_password(request):
    generated_password = None

    if request.method == 'POST':
        length = request.POST.get('length')
        caps = request.POST.get('caps')
        numbers = request.POST.get('numbers')
        special_chars = request.POST.get('special_chars')
        print(length)
        chars = string.ascii_lowercase
        if length.isdigit():  # Check if 'length' is a valid integer
            length = int(length)
            if length:
                if caps:
                    chars += string.ascii_uppercase
                if numbers:
                    chars += string.digits
                if special_chars:
                    chars += string.punctuation
                    
                generated_password = ''.join(random.choice(chars) for _ in range(length))
    return render(request, 'index.html', {'password': generated_password})