from rest_framework import generics, filters, pagination
from django.db.models import Q
from users.authentication import APIKeyAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer


# Define a custom pagination class for books and authors lists.
class CustomPagination(pagination.PageNumberPagination):
    page_size = 10  # Default page size
    page_size_query_param = 'page_size'  # Parameter for custom page size in GET request
    max_page_size = 100  # Maximum page size cap
    

class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()  # Queryset for retrieving all books
    serializer_class = BookSerializer  # Serializer class for books
    filter_backends = [filters.SearchFilter]  # Enable search filter
    search_fields = ['title', 'author__name']  # Fields to search against
    pagination_class = CustomPagination  # Use custom pagination class
    authentication_classes = [SessionAuthentication, APIKeyAuthentication]

    # Customize queryset based on 'q' parameter in GET request
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.query_params.get('q', None)
        if query:
            # Filter by book title and author name containing the query
            queryset = queryset.filter(Q(title__icontains=query) | Q(author__name__icontains=query))
        return queryset
    

class BookRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()  # Queryset for retrieving all books
    serializer_class = BookSerializer  # Serializer class for books
    authentication_classes = [SessionAuthentication, APIKeyAuthentication]
    

class AuthorListCreate(generics.ListCreateAPIView):
    queryset = Author.objects.all()  # Queryset for retrieving all authors
    serializer_class = AuthorSerializer  # Serializer class for authors
    filter_backends = [filters.SearchFilter]  # Enable search filter
    search_fields = ['name']  # Fields to search against
    pagination_class = CustomPagination  # Use custom pagination class
    authentication_classes = [SessionAuthentication, APIKeyAuthentication]
    

class AuthorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()  # Queryset for retrieving all authors
    serializer_class = AuthorSerializer  # Serializer class for authors
    authentication_classes = [SessionAuthentication, APIKeyAuthentication]
