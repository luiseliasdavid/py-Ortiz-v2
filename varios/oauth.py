# oauth_example/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout

def home(request):
    return render(request, 'home.html')

def profile(request):
    if not request.user.is_authenticated:
        return redirect('home')
    return render(request, 'profile.html')

def logout_view(request):
    auth_logout(request)
    return redirect('home')

def auth(request):
    # Redirigir a la página de autorización de Google
    return redirect('/auth/login/google-oauth2/')
