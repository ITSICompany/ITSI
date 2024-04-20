from django.shortcuts import render
from ITSI_ID.models import Users

def index(request):
    return render(request, 'service/index.html')

def start(request):
    return render(request, 'start/index.html')

def documentation(request):
    return render(request, 'documentation/index.html')

def cabinet(request):
    data = Users.objects.get(id=1)
    
    user = {
        'data': data
    }

    return render(request, 'cabinet/index.html', context=user)