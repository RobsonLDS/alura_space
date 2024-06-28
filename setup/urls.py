from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('apps.galeria.urls')), #* Caminho das URLS da Galeria
    path('', include('apps.usuarios.urls')), #* Caminho das URLS do Usuarios
    path('', include('apps.blog.urls')), #* Caminho das URLS do Blog
    path('', include('apps.mensagens_email.urls')), #* Caminho das URLS do Blog

    path('ckeditor/', include('ckeditor_uploader.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
