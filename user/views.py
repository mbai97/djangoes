from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import SESSION_KEY, authenticate, login
from django.contrib.auth.models import User, auth
from django.conf import settings
from django.contrib import messages
from django.utils import timezone
from random import randint

def anonymous_required(function=None, redirect_url=None):
    if not redirect_url:
        redirect_url = 'dashboard'
        
        actual_decorator = user_passes_test(
            lambda u: u.is_anonymous,
            login_url=redirect_url
        )
        
        if function:
            return actual_decorator(function)
        return actual_decorator
    
@login_required
def logout(request):
    auth.logout(request)
    return redirect('login')

@anonymous_required
def login(request):
    
    return render (request, 'user/login.html', {})
    
    
@anonymous_required
def register(request):
    
    return render (request, 'user/register.html', {})

# @login_required
@anonymous_required
def dashboard(request):
    
    return render (request, 'user/dash.html', {})

# @login_required    
@anonymous_required
def index(request):
    return render (request, 'user/index.html', {})

# @login_required
@anonymous_required
def jewellery(request):
    return render (request, 'user/jewellery.html')

# @login_required
@anonymous_required
def electronic(request):
    return render (request, 'user/electronic.html')

# @login_required
@anonymous_required
def fashion(request):
    return render (request, 'user/fashion.html')


    
    