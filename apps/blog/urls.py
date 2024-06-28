from django.urls import path
from apps.blog.views import \
    home

urlpatterns = [
    path('blog.html', home, name="blog")
]