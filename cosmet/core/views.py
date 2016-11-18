from django.shortcuts import render

def home(request):
    return render(request, 'core/index.html')

def login(request):
    return render(request, 'core/login.html')

def gerencia(request):
    return render(request, 'core/admin.html')
