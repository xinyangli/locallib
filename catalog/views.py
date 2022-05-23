from django.shortcuts import render
from django.db.models import F, Q
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Book, Author, BookInstance, Record

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
    borrow_instance = request.POST.get('instance', None)
    book = Book.objects.get(bookId=bookId)
    book_instances = BookInstance.objects.filter(book=book)
    if borrow_instance is not None:
        BookInstance.objects.get(binstanceId=borrow_instance).borrow(request.user)
    context = {
        "book": book,
        "book_instances": book_instances,
        "borrow_instance": borrow_instance,
    }
    return render(request, 'book_detail.html', context=context)


def author(request):
    author_list = Author.objects.all().annotate(title=F('name'), id=F('authorId'))
    url = request.get_full_path()
    context = {
        "url": url,
        "card_list": author_list,
        "no_item_warning": "There is no author information"
    }
    return render(request, 'author.html', context=context)


def author_detail(request, authorId):
    author = Author.objects.get(authorId=authorId)
    book_list = Book.objects.filter(author=author).all().annotate(id=F('bookId'))
    book_url = reverse('book')
    context = {
        "url": book_url,
        "card_list": book_list,
        "author": author,
    }
    return render(request, 'author_detail.html', context=context)


def search(request):
    s = request.GET.get('s', None)
    if s is None:
        return render(request, 'search.html')
    book_list = Book.objects.filter(Q(title__contains=s) | Q(genre__name__contains=s)).distinct()
    author_list = Author.objects.filter(name__contains=s).annotate(title=F('name'))
    context = {
        "book_list": book_list,
        "author_list": author_list,
        "query": s
    }
    return render(request, 'search.html', context=context)


def info(request):
    book_instances = Record.objects.filter(reader=request.user)
    context = {
        'book_instances': book_instances,
    }
    return render(request, 'info.html', context=context)
