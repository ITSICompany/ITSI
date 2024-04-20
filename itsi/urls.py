from django.contrib import admin
from django.urls import path
from API.views import index, start, documentation

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/service/', index, name='service'),
    path('api/start/', start, name='start'),
    path('api/documentation/', documentation, name='documentation'),
]
