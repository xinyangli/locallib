from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth import get_user_model
from datetime import datetime, timedelta
from . import *


class Book(models.Model):
    bookId = models.AutoField(primary_key=True)
    ISBN = models.CharField(max_length=13)
    title = models.CharField(max_length=45)
    record = models.ForeignKey('Record', on_delete=models.SET_NULL, null=True, blank=True)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True, blank=True)
    press = models.ForeignKey('Press', on_delete=models.SET_NULL, null=True, blank=True)
    # genreId = models.ForeignKey('Genre', on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='books', blank=True, default="cover.jpg")
    genre = models.ManyToManyField(to='Genre', related_name='Book')

    class Meta:
        ordering = ['bookId']

    def __str__(self):
        return "{} - {}".format(self.title, self.ISBN)


class BookInstance(models.Model):
    binstanceId = models.AutoField(primary_key=True)
    # on_shelf = models.BooleanField(default=True)
    position = models.CharField(max_length=45)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)

    class Meta:
        pass

    def __str__(self):
        return self.book.title + str(self.binstanceId)

    def borrow(self, user):
        record = {
            "reader": user,
            "binstance": self,
            "start": datetime.now(),
            "due": datetime.now() + timedelta(days=30)
        }
        record = Record.objects.create(**record)
        record.save()

    @property
    def on_shelf(self):
        record = Record.objects.get(binstance=self, returned=False)
        if record:
            return True
        return False


class Press(models.Model):
    pressId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=45, null=True, blank=True)

    def __str__(self):
        return self.name


class Reader(models.Model):
    readerId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    birth = models.DateField(null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Genre(models.Model):
    genreId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)

    class Meta:
        ordering = ['genreId']

    def __str__(self):
        return self.name


class Author(models.Model):
    authorId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    gender = models.CharField(choices=[('f', 'Female'), ('m', 'Male')], max_length=1)
    birth = models.DateField(null=True, blank=True)
    death = models.DateField(null=True, blank=True)
    nationality = CountryField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='authors', blank=True, default="author.png")

    class Meta:
        ordering = ['authorId']

    def __str__(self):
        return "{},{}".format(self.name, self.nationality)


class Record(models.Model):
    recordId = models.AutoField(primary_key=True)
    reader = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    binstance = models.ForeignKey('BookInstance', on_delete=models.CASCADE)
    start = models.DateTimeField()
    due = models.DateTimeField(null=True)
    returned = models.BooleanField(default=False)

    def __str__(self):
        return str(self.recordId)
