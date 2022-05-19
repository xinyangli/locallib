from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('books/', views.book, name='book'),
    path('books/<int:bookId>/', views.book_detail, name='book-detail'),
    path('authors/', views.author, name='author'),
]