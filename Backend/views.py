from django.shortcuts import render
from blog.models import BlogPost


def home_page(request):
    qs = BlogPost.objects.last()
    context = {'post': qs}
    return render(request, 'home.html', context)


def author_page_tymek(request):
    return render(request, 'tymek.html')


def author_page_szymon_w(request):
    return render(request, 'szymonw.html')


def author_page_szymon_f(request):
    return render(request, 'szymonf.html')
