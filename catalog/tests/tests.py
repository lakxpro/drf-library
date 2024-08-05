from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from ..models import Author, Book, AuthorBook
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class APITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        self.author = Author.objects.create(first_name='Evangelos', last_name='katsaros', date_of_birth='1996-07-08')
        self.book = Book.objects.create(name='Test Book', isbn='1234567890', year=2020)
        self.author_book = AuthorBook.objects.create(author=self.author, book=self.book)

    def test_author_list(self):
            response = self.client.get(reverse('author'))
            self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_author_detail_get(self):
        response = self.client.get(reverse('author-detail', kwargs={'pk': self.author.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_author_detail_put(self):
        data = {'first_name': 'lakx', 'last_name': 'lakx', 'date_of_birth': '2004-01-01'}
        response = self.client.put(reverse('author-detail', kwargs={'pk': self.author.pk}), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_author_detail_delete(self):
        response = self.client.delete(reverse('author-detail', kwargs={'pk': self.author.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_author_create(self):
        data = {'first_name': 'lakx', 'last_name': 'lakx', 'date_of_birth': '2004-01-01'}
        response = self.client.post(reverse('author'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_book_list(self):
        response = self.client.get(reverse('book'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_book_detail_get(self):
        response = self.client.get(reverse('book-detail', kwargs={'pk': self.book.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_book_detail_put(self):
        data = {'name': 'lakx', 'isbn': 'lakx', 'year': 2004}
        response = self.client.put(reverse('book-detail', kwargs={'pk': self.book.pk}), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_book_detail_patch(self):
        data = {'name': 'lakx', 'isbn': 'lakx', 'year': 2004}
        response = self.client.put(reverse('book-detail', kwargs={'pk': self.book.pk}), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_book_detail_delete(self):
        response = self.client.delete(reverse('book-detail', kwargs={'pk': self.book.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_book_create(self):
        data = {'name': 'lakx', 'isbn': 'lakx', 'year': 2004}
        response = self.client.post(reverse('book'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_author_book_list(self):
        response = self.client.get(reverse('author-book'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_author_book_detail_get(self):
        response = self.client.get(reverse('author-book-detail', kwargs={'pk': self.author_book.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_author_book_detail_put(self):
        author = Author.objects.create(first_name='lakx', last_name='lakx', date_of_birth='1997-07-08')
        data = {'book': self.book.pk, 'author': author.pk}
        response = self.client.put(reverse('author-book-detail', kwargs={'pk': self.author_book.pk}), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_author_book_detail_patch(self):
        author = Author.objects.create(first_name='lakx', last_name='lakx', date_of_birth='1997-07-08')
        data = {'book': self.book.pk, 'author': author.pk}
        response = self.client.put(reverse('author-book-detail', kwargs={'pk': self.author_book.pk}), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_author_book_detail_delete(self):
        response = self.client.delete(reverse('author-book-detail', kwargs={'pk': self.author_book.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_author_book_create(self):
        book = Book.objects.create(name='Test Book2', isbn='1234567891', year=2021)
        author = Author.objects.create(first_name='lakx', last_name='lakx', date_of_birth='1997-07-08')
        data = {'book': book.pk, 'author': author.pk}
        response = self.client.post(reverse('author-book'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)