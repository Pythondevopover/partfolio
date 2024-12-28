from django.urls import path
from .views import blog_list, blog_detail

urlpatterns = [
    path('', blog_list, name='blog_list'),  # Bloglar ro'yxati
    path('<int:post_id>/', blog_detail, name='blog_detail'),  # Blog post detallari
]