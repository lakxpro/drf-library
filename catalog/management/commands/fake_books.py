from typing import Any
from django.core.management.base import BaseCommand
from catalog.models import Book
from django.utils import timezone
from faker import Faker
import random

class Command(BaseCommand):
    help = "Populate Books table"
    
    def handle(self, *args: Any, **options: Any):
        fake = Faker()

        for i in range(50):
            try:
                Book.objects.create(name=fake.word(),isbn=fake.sbn9(),year=random.randint(1600, timezone.now().year))
                i += 1
            except BaseException as e:
                print(e)
                i -= 1