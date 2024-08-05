from typing import Any
from django.core.management.base import BaseCommand
from catalog.models import Author
from faker import Faker

class Command(BaseCommand):
    help = "Populate Authors table"
    
    def handle(self, *args: Any, **options: Any):
        fake = Faker()

        for i in range(50):
            try:
                Author.objects.create(first_name=fake.first_name(),last_name=fake.last_name(),date_of_birth=fake.date())
                i += 1
            except BaseException as e:
                print(e)
                i -= 1
        