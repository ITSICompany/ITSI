from django.shortcuts import render

def index(request):
    return render(request, 'service/index.html')

def start(request):
    return render(request, 'start/index.html')

def documentation(request):
    return render(request, 'documentation/index.html')