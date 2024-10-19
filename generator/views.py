import random
import string
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def password(request):
    # Get parameters from GET request for password customization
    length = int(request.GET.get('length', 12))
    include_uppercase = request.GET.get('uppercase')
    include_numbers = request.GET.get('numbers')
    include_special = request.GET.get('special')

    # Define character sets
    characters = list(string.ascii_lowercase)
    
    if include_uppercase:
        characters.extend(list(string.ascii_uppercase))
    if include_numbers:
        characters.extend(list(string.digits))
    if include_special:
        characters.extend(list('!@#$%^&*()-_=+'))

    # Generate random password
    generated_password = ''.join(random.choice(characters) for _ in range(length))
    
    return render(request, 'password.html', {'password': generated_password})
