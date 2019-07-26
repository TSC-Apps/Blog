"""Backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from .views import home_page, author_page_tymek, author_page_szymon_f, author_page_szymon_w

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home-page'),
    path('tymoteusz-frankiewcz/', author_page_tymek, name='tymek'),
    path('szymon-wisniewski/', author_page_szymon_w, name='szymonw'),
    path('szymon-frankiewicz/', author_page_szymon_f, name='szymonf'),
    re_path(r'^tinymce/', include('tinymce.urls')),

    # all urls from blog app, which is plugable app module
    # first arguments sets it like this: blog/edit...
    path('blog/', include('blog.urls'))
]
