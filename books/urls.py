from django.urls import path
from .views import (
    BookListCreate,
    BookRetrieveUpdateDestroy,
    AuthorListCreate,
    AuthorRetrieveUpdateDestroy
    )

urlpatterns = [
    path('books/', BookListCreate.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroy.as_view(), name='book-retrieve-update-destroy'),
    path('authors/', AuthorListCreate.as_view(), name='author-list-create'),
    path('authors/<int:pk>/', AuthorRetrieveUpdateDestroy.as_view(), name='author-retrieve-update-destroy'),
]