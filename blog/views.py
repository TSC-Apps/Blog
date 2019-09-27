from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import BlogPost


# Create your views here.


def blog_post_list_view(request):
    """List outs blog posts, may search them"""
    qs = BlogPost.objects.all().order_by('-date')
    if request.method == 'GET':
        search_phrase = request.GET.get('search')
        if search_phrase:
            qs = BlogPost.objects.filter(
                Q(content__icontains=search_phrase) |
                Q(title__icontains=search_phrase) |
                Q(user__username__icontains=search_phrase)).distinct()

        category = request.GET.get('category')
        if category:
            qs = BlogPost.objects.filter(article_type=category)

    paginator = Paginator(qs, 5)
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
