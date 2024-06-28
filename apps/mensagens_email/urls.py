
from django.urls import path
from apps.mensagens_email.views import \
    post_mensagens
urlpatterns = [
    path('mensagens_email', post_mensagens, name='mensagens_email'),
]