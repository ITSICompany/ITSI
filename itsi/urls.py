from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static 
from API.views import index, start, documentation, cabinet, auth, AnaliticAPIView, UsersAPIUpdate
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/service/', index, name='service'),
    path('api/start/', start, name='start'),
    path('api/documentation/', documentation, name='documentation'),
    path('api/cabinet/', cabinet, name='cabinet'),
    path('api/auth/', auth, name='auth'),
    
    # API =============================
    
    path('api/v1/analitic/<int:pk>/', AnaliticAPIView.as_view()),
    path('api/v1/user/<int:pk>/', UsersAPIUpdate.as_view()),
    
    # API Token ============
    # path('api/v1/auth/', include('djoser.urls')),
    # re_path(r'^auth/', include('djoser.urls.authtoken')),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # ======================
    
    # =================================
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)