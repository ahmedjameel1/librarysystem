from rest_framework import status
import pytest
from model_bakery import baker
from django.contrib.auth.models import User
from users.models import APIKey
from books.models import Book, Author

@pytest.mark.django_db
class TestBookCreate:
    def test_create_book_no_api_key_returns_403(self, api_client):
        data = {
            'title': 'Happy',
            'isbn': '9781234567897',
            'published_year': 2024,
            'author': 1
        }
        
        response = api_client.post('/api/books/', data=data)

        assert response.status_code == status.HTTP_403_FORBIDDEN
        
    def test_create_book_with_api_key_returns_201(self, api_client):
        data = {
            "title": "Happy",
            "isbn": "9781688347847", # this is uniqeue so each time use a different isbn.
            "published_year": 2024,
            "author": baker.make(Author).id
        }
        api_key = baker.make(APIKey).key
        
        response = api_client.post('/api/books/', data=data,
                                   headers={'APIKEY': api_key})

        assert response.status_code == status.HTTP_201_CREATED
