from django.shortcuts import render, get_object_or_404
from .models import BlogPost


# Create your views here.

def blog_post_detail_page(request, slug):
    """ Gets blog post object with given slug and displays it, or gives 404"""
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_post_detail.html'
    context = {"object": obj}
    return render(request, template_name, context)
