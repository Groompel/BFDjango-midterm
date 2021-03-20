from main.views import BookDetailsModelViewSet, BookModelViewSet, JournalDetailsModelViewSet, JournalModelViewSet
from django.urls import path

urlpatterns = [
    path('books/', BookModelViewSet.as_view({'get': 'list', })),
    path('books/<int:id>',
         BookDetailsModelViewSet.as_view({'get': 'retrieve'})),
    path('journals/', JournalModelViewSet.as_view({'get': 'list'})),
    path('journals/<int:id>',
         JournalDetailsModelViewSet.as_view({'get': 'retrieve'}))
]
