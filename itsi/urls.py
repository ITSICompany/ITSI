from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from API.views import index, start, documentation, cabinet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/service/', index, name='service'),
    path('api/start/', start, name='start'),
    path('api/documentation/', documentation, name='documentation'),
    path('api/cabinet/', cabinet, name='cabinet'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)