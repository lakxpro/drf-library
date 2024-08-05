from rest_framework.test import APITestCase
from rest_framework import status
from ..models import Book
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class BookAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        self.book = Book.objects.create(name='Test Book', isbn='1234567890', year=2020)
        self.book_list_url = '/api/book/'
        self.book_detail_url = f'/api/book/{self.book.pk}/'

    def test_book_list(self):
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Test Book')

    def test_book_get(self):
        response = self.client.get(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Test Book')

    def test_book_put(self):
        data = {'name': 'Lakx', 'isbn': 'Lakx', 'year': 2004,'author': []}
        response = self.client.put(self.book_detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Lakx')

    def test_book_patch(self):
        data = {'name': 'Lakx', 'isbn': 'Lakx', 'year': 2004}
        response = self.client.patch(self.book_detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Lakx')

    def test_book_delete(self):
        response = self.client.delete(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_book_create(self):
        data = {'name': 'Lakx', 'isbn': 'Lakx', 'year': 2004,}
        response = self.client.post(self.book_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED) 

