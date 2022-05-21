from django.contrib import admin
from .models import Book, Reader, Genre, Author, Press, Record, BookInstance


class BookAdmin(admin.ModelAdmin):
    pass


class ReaderAdmin(admin.ModelAdmin):
    pass


class GenreAdmin(admin.ModelAdmin):
    pass


class AuthorAdmin(admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(Reader, ReaderAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Press)
admin.site.register(Record)
admin.site.register(BookInstance)