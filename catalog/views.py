from django.shortcuts import render
from django.db.models import F
from .models import Book, Author


def index(request):
    """View funciton for home page of site."""
    return render(request, 'index.html')


def book(request):
    book_list = Book.objects.all()
    context = {
        "card_list": book_list,
        "no_item_warning": "There are no books in the library"
    }
    return render(request, 'book.html', context=context)


def author(request):
    author_list = Author.objects.all().annotate(title=F('name'))
    context = {
        "card_list": author_list,
        "no_item_warning": "There is no author information"
    }
    return render(request, 'author.html', context=context)


def search(request):
    return render(request, 'search.html')