from django.urls import path
from .views import blog_list, blog_detail
from django.shortcuts import render

def custom_page_not_found(request, exception):
    return render(request, "404.html", status=404)

handler404 = custom_page_not_found
urlpatterns = [
    path('', blog_list, name='blog_list'),  # Bloglar ro'yxati
    path('<int:post_id>/', blog_detail, name='blog_detail'),  # Blog post detallari
]
