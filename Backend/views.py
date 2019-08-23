from django.shortcuts import render
from blog.models import BlogPost


def home_page(request):
    qs = BlogPost.objects.last()
    last_three_posts = BlogPost.objects.all().order_by('-id')[:3]
    context = {'post': qs, 'last_three_posts': last_three_posts}
    return render(request, 'home.html', context)


def author_page_tymek(request):
    last_three_posts = BlogPost.objects.filter(user__username='tymoteusz-frankiewicz').order_by('-id')[:3]
    context = {'last_three_posts': last_three_posts}
    return render(request, 'tymek.html', context)


def author_page_szymon_w(request):
    last_three_posts = BlogPost.objects.filter(user__username='szymon-wisniewski').order_by('-id')[:3]
    context = {'last_three_posts':last_three_posts}
    return render(request, 'szymonw.html', context)


def author_page_szymon_f(request):
    last_three_posts = BlogPost.objects.filter(user__username='szymon-frankiewicz').order_by('-id')[:3]
    context = {'last_three_posts': last_three_posts}
    return render(request, 'szymonf.html', context)
