from typing import Any
from django.core.management.base import BaseCommand
from catalog.models import Book, Author
from django.utils import timezone
from faker import Faker
import random

class Command(BaseCommand):
    help = "Populate Books table"
    
    def handle(self, *args: Any, **options: Any):
        fake = Faker()
        authors = list(Author.objects.all().values_list('pk',flat=True))
        for i in range(50):
            try:
                book = Book.objects.create(name=fake.word(),isbn=fake.sbn9(),year=random.randint(1600, timezone.now().year))
                book.author.add(*random.sample(authors, k=random.randint(1, 3)))
                book.save()
                i += 1
            except BaseException as e:
                print(e)
                i -= 1