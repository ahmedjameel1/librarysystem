from rest_framework import status
import pytest
from model_bakery import baker
from django.contrib.auth.models import User
from users.models import APIKey
from books.models import Book, Author

@pytest.mark.django_db
class TestBookList:
    def test_books_list_no_api_key_returns_403(self, api_client):
        response = api_client.get('/api/books/')
        
        assert response.status_code == status.HTTP_403_FORBIDDEN
        
    def test_books_list_with_api_key_returns_200(self, api_client):
        api_key = baker.make(APIKey).key
        
        response = api_client.get('/api/books/', headers={'APIKEY': api_key})
        
        assert response.status_code == status.HTTP_200_OK
        
@pytest.mark.django_db
class TestBookCRUD: # create read update delete
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
        
    def test_book_read_no_api_key_returns_403(self, api_client):
        book = baker.make(Book, id=1)
        
        response = api_client.get('/api/books/1/')
        
        assert response.status_code == status.HTTP_403_FORBIDDEN
        
    def test_book_read_with_api_key_returns_200(self, api_client):
        book = baker.make(Book, id=1)
        api_key = baker.make(APIKey).key
        
        response = api_client.get('/api/books/1/', headers={'APIKEY': api_key})
        
        assert response.status_code == status.HTTP_200_OK
        
    def test_update_book_returns_200(self, api_client):
        book = baker.make(Book, id=1, title='Happy')
        api_key = baker.make(APIKey)
        data = {
            'title': 'not happy'
        }
        
        response = api_client.patch('/api/books/1/', data, headers={'APIKEY': api_key})
        
        assert response.status_code == status.HTTP_200_OK
        assert response.json()['title'] == 'not happy'

    def test_delete_book_returns_204(self, api_client):
        book = baker.make(Book, id=1, title='Happy')
        api_key = baker.make(APIKey)
        
        response = api_client.delete('/api/books/1/', headers={'APIKEY': api_key})
        
        assert response.status_code == status.HTTP_204_NO_CONTENT