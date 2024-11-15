from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.

def all_blogs(request):
    blog = Blog.objects.order_by('-date')[:3] 
    # Para que só se mostre un número determinado de entradas --> 
    #   [: numeroEntradasVisibles]
    # Para que a orde sexa descendente engadimos un '-' antes do campo
    return render(request, 'blog/all_blogs.html', {'Blog':blog})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'id':blog_id})