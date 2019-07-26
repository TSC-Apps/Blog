from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    return render(request, 'home.html')


def author_page_tymek(request):
    return render(request, 'tymek.html')


def author_page_szymon_w(request):
    return render(request, 'szymonw.html')


def author_page_szymon_f(request):
    return render(request, 'szymonf.html')
