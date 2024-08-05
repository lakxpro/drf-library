from typing import Any
from django.core.management.base import BaseCommand
from catalog.models import Author, Book, AuthorBook
import random

class Command(BaseCommand):
    help = "Populate Authors table"
    
    def handle(self, *args: Any, **options: Any):
        books = Book.objects.all()
        authors = list(Author.objects.all())
        for book in books:
            try:
                AuthorBook.objects.create(book=book,author=random.choice(authors))
            except BaseException as e:
                print(e)
        