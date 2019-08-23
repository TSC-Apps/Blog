from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import BlogPost


# Create your views here.


def blog_post_list_view(request):
    """List outs blog posts, may search them"""
    qs = BlogPost.objects.all().order_by('-date')
    paginator = Paginator(qs, 1)
    page = request.GET.get('page')
    objects = paginator.get_page(page)
    template_name = 'blog/list.html'

    last_three_posts = BlogPost.objects.all().order_by('-id')[:3]
    context = {'object_list': objects, 'last_three_posts': last_three_posts}
    return render(request, template_name, context)


def blog_post_detail_view(request, slug):
    """ Gets blog post object with given slug and displays it, or gives 404"""
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/detail.html'
    context = {'post': obj}
    return render(request, template_name, context)
