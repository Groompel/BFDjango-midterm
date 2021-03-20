from rest_framework.utils import model_meta
from main.models import Book, BookSerializer, Journal, JournalSerializer
from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.


class BookModelViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_url_kwarg = 'id'

    def get(self, req, *args, **kwargs):
        return self.list(req, *args, **kwargs)

    def post(self, req, *args, **kwargs):
        return self.create(req, *args, **kwargs)


class BookDetailsModelViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_url_kwarg = 'id'

    def put(self, req, *args, **kwargs):
        return self.update(req, *args, **kwargs)

    def delete(self, req, *args, **kwargs):
        return self.destroy(req, *args, **kwargs)


class JournalModelViewSet(viewsets.ModelViewSet):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer

    def get(self, req, *args, **kwargs):
        return self.list(req, *args, **kwargs)

    def post(self, req, *args, **kwargs):
        return self.create(req, *args, **kwargs)


class JournalDetailsModelViewSet(viewsets.ModelViewSet):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    lookup_url_kwarg = 'id'

    def put(self, req, *args, **kwargs):
        return self.update(req, *args, **kwargs)

    def delete(self, req, *args, **kwargs):
        return self.destroy(req, *args, **kwargs)
