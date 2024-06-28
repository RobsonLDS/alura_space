from django.shortcuts import render
from apps.blog.models import Blog
from apps.blog.forms import BlogForm

def home(request):
    data = Blog.objects.all()
    
    form = BlogForm
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid:
            form.save()
            form = BlogForm

    context={"data": data, "form": form}
    return render(request,"blog/blog.html",context)
