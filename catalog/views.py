from django.shortcuts import render


def index(request):
    """View funciton for home page of site."""
    return render(request, 'index.html')


def book(request):
    return render(request, 'book.html')


def author(request):
    return render(request, 'author.html')


def search(request):
    return render(request, 'search.html')