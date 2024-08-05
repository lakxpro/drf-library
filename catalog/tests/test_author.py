from rest_framework.test import APITestCase
from rest_framework import status
from ..models import Author
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class AuthorAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        self.author = Author.objects.create(first_name='Evangelos', last_name='Katsaros', date_of_birth='1996-07-08')
        self.author_list_url = '/api/author/'
        self.author_detail_url = f'/api/author/{self.author.pk}/'

    def test_author_list(self):
        response = self.client.get(self.author_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Evangelos')

    def test_author_get(self):
        response = self.client.get(self.author_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Evangelos')

    def test_author_put(self):
        data = {'first_name': 'Lakx', 'last_name': 'Lakx', 'date_of_birth': '2004-01-01'}
        response = self.client.put(self.author_detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_author_delete(self):
        response = self.client.delete(self.author_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_author_create(self):
        data = {'first_name': 'Lakx', 'last_name': 'Lakx', 'date_of_birth': '2004-01-01'}
        response = self.client.post(self.author_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
