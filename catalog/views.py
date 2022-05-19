from django.shortcuts import render
from django.db.models import F
from .models import Book, Author


def index(request):
    """View funciton for home page of site."""
    return render(request, 'index.html')


def book(request):
    book_list = Book.objects.all().annotate(id=F('bookId'))
    url = request.get_full_path()
    context = {
        "url": url,
        "card_list": book_list,
        "no_item_warning": "There are no books in the library"
    }
    return render(request, 'book.html', context=context)


def book_detail(request, bookId):
    book = Book.objects.get(bookId=bookId)
    context = {
        "book": book,
    }
    return render(request, 'book_detail.html', context=context)


def author(request):
    author_list = Author.objects.all().annotate(title=F('name'))
    context = {
        "card_list": author_list,
        "no_item_warning": "There is no author information"
    }
    return render(request, 'author.html', context=context)


def search(request):
    s = request.GET.get('s', None)
    if s is None:
        return render(request, 'search.html')
    book_list = Book.objects.filter(title__contains=s)
    author_list = Author.objects.filter(name__contains=s).annotate(title=F('name'))
    context = {
        "book_list": book_list,
        "author_list": author_list,
        "query": s
    }
    return render(request, 'search.html', context=context)