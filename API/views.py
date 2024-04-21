from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from ITSI_ID.models import Users
from .serializers import AnaliticSerializer, UsersSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class AnaliticAPIView(ListAPIView):
    serializer_class = AnaliticSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        user_id = self.request.user.id
        return Users.objects.filter(id=user_id)

class UsersAPIUpdate(ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = (IsAuthenticated,)

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

def auth(request):
    if 'register' in request.POST:
        pass
    
    return render(request, 'auth/index.html')