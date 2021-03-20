from django.db import models
from rest_framework import serializers

# Create your models here.

JOURNAL_TYPE_CHOICES = [(0, 'Bullet'), (1, 'Food'),
                        (2, 'Travel'), (3, 'Sport')]


class BookJournalBase(models.base.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    price = models.FloatField(verbose_name='Price')
    description = models.TextField(verbose_name='Description')
    created_at = models.DateTimeField(
        verbose_name='Created at', auto_now_add=True)


class Book(BookJournalBase):
    num_pages = models.IntegerField(verbose_name='Number of pages')
    genre = models.CharField(verbose_name='Genre', max_length=100)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.name


class Journal(BookJournalBase):
    journal_type = models.IntegerField(
        verbose_name='Type', choices=JOURNAL_TYPE_CHOICES)
    publisher = models.CharField(verbose_name='Publisher', max_length=100)

    class Meta:
        verbose_name = 'Journal'
        verbose_name_plural = 'Journals'

    def __str__(self):
        return self.name


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'name', 'price', 'description',
                  'created_at', 'num_pages', 'genre')


class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = ('id', 'name', 'price', 'description',
                  'created_at', 'journal_type', 'publisher')
