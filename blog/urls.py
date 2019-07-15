from django.urls import path
from .views import (
    blog_post_detail_view,
    blog_post_list_view,
)

urlpatterns = [
    path('', blog_post_list_view, name='blog'),
    path('<str:slug>/', blog_post_detail_view),
]
