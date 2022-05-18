from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    path('books', views.book, name='book'),
    path('authors', views.author, name='author'),
]