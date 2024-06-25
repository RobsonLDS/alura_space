from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('galeria.urls')), #* Caminho das URLS da Galeria
    
    path('',include('usuarios.urls')), #* Caminho das URLS do Usuarios

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
