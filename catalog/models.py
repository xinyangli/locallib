from django.db import models
from django_countries.fields import CountryField


class Book(models.Model):
    # Fields here
    bookId = models.AutoField(primary_key=True)
    ISBN = models.CharField(max_length=13)
    title = models.CharField(max_length=45)
    recordId = models.ForeignKey('Record', on_delete=models.SET_NULL, null=True, blank=True)
    authorId = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True, blank=True)
    pressId = models.ForeignKey('Press', on_delete=models.SET_NULL, null=True, blank=True)
    genreId = models.ForeignKey('Genre', on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(null=True)
    image = models.ImageField(null=True)

    class Meta:
        ordering = ['bookId']

    def __str__(self):
        return "{} - {}".format(self.title, self.ISBN)


class Press(models.Model):
    pressId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=45)

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
    image = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = ['authorId']

    def __str__(self):
        return "{},{}".format(self.name, self.nationality)


class Record(models.Model):
    recordId = models.IntegerField(primary_key=True)
    readerId = models.ForeignKey('Reader', on_delete=models.RESTRICT)
    bookId = models.ForeignKey('Book', on_delete=models.RESTRICT)
    start = models.DateTimeField()
    due = models.DateTimeField(null=True)

    def __str__(self):
        return str(self.recordId)
