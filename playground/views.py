from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def index(request):
    # return render(request, 'index.html', {'name': 'Mbai'})

def login(request):
    return render (request, 'login.html')

def dashboard(request):
    return render (request, 'dash.html')

def logout(request): 
    return render (request, 'login.html')


def jewellery(request):
    return render (request, 'jewellery.html')

def electronic(request):
    return render (request, 'electronic.html')

def fashion(request):
    return render (request, 'fashion.html')

def index(request):
    return render (request, 'index.html')