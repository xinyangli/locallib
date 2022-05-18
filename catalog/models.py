from django.db import models

class Book(models.Model):
    # Fields here
    id = models.IntegerField(primary_key=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.id


class Reader(models.Model):
    id = models.IntegerField(primary_key=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.id


class Genre(models.Model):
    id = models.IntegerField(primary_key=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.id


class Author(models.Model):
    id = models.IntegerField(primary_key=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.id
