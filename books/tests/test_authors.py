from rest_framework import status
import pytest
from model_bakery import baker
from django.contrib.auth.models import User
from users.models import APIKey
from books.models import Author

@pytest.mark.django_db
class TestAuthorList:
    def test_authors_list_no_api_key_returns_403(self, api_client):
        response = api_client.get('/api/authors/')
        
        assert response.status_code == status.HTTP_403_FORBIDDEN
        
    def test_authors_list_with_api_key_returns_200(self, api_client):
        api_key = baker.make(APIKey).key
        
        response = api_client.get('/api/authors/', headers={'APIKEY': api_key})
        
        assert response.status_code == status.HTTP_200_OK
        
@pytest.mark.django_db
class TestAUthorCRUD: # create read update delete
    def test_create_author_no_api_key_returns_403(self, api_client):
        data = {
            'name': 'Happy',
            'birth_year': '2000',
        }
        
        response = api_client.post('/api/authors/', data=data)

        assert response.status_code == status.HTTP_403_FORBIDDEN
        
    def test_create_author_with_api_key_returns_201(self, api_client):
        data = {
            'name': 'Happy',
            'birth_year': '2000',
        }
        api_key = baker.make(APIKey).key
        
        response = api_client.post('/api/authors/', data=data,
                                   headers={'APIKEY': api_key})

        assert response.status_code == status.HTTP_201_CREATED
        
    def test_author_read_no_api_key_returns_403(self, api_client):
        author = baker.make(Author, id=1)
        
        response = api_client.get('/api/authors/1/')
        
        assert response.status_code == status.HTTP_403_FORBIDDEN
        
    def test_author_read_with_api_key_returns_200(self, api_client):
        author = baker.make(Author, id=1)
        api_key = baker.make(APIKey).key
        
        response = api_client.get('/api/authors/1/', headers={'APIKEY': api_key})
        
        assert response.status_code == status.HTTP_200_OK
        
    def test_update_author_returns_200(self, api_client):
        author = baker.make(Author, id=1, name='Happy')
        api_key = baker.make(APIKey)
        data = {
            'name': 'not happy',
            'birth_year': '2000',
        }
        
        response = api_client.patch('/api/authors/1/', data, headers={'APIKEY': api_key})
        
        assert response.status_code == status.HTTP_200_OK
        assert response.json()['name'] == 'not happy'

    def test_delete_author_returns_204(self, api_client):
        author = baker.make(Author, id=1)
        api_key = baker.make(APIKey)
        
        response = api_client.delete('/api/authors/1/', headers={'APIKEY': api_key})
        
        assert response.status_code == status.HTTP_204_NO_CONTENT