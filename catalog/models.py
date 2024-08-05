from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
import datetime

def validate_year(value):
    current_year = timezone.now().year
    if value > current_year:
        raise ValidationError(f"The year {value} cannot be in the future.")
    
def validate_date_of_birth(value):
    current_date = datetime.date.today()
    if value > current_date:
        raise ValidationError(f"Date of birth {value} cannot be in the future.")
    
class Author(models.Model):
    first_name = models.CharField(max_length=255,verbose_name="first name")
    last_name = models.CharField(max_length=255,verbose_name="last name")
    date_of_birth = models.DateField(validators=[validate_date_of_birth])

    class Meta:
        ordering = ['id']
        verbose_name = "author"
        verbose_name_plural = "authors"
        
    def __str__(self):
        return f"Author {self.first_name} {self.last_name} born in {self.date_of_birth}"
    


class Book(models.Model):
    name = models.CharField(max_length=255,verbose_name="name")
    isbn = models.CharField(max_length=20,unique=True,verbose_name="ISBN")
    year = models.PositiveIntegerField(verbose_name="release year", validators=[validate_year])

    class Meta:
        ordering = ['id']
        verbose_name = "book"
        verbose_name_plural = "books"

    def __str__(self) -> str:
        return f"Book {self.name} isbn {self.isbn} year {self.year}"
    
class AuthorBook(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']
        unique_together=["author","book"]
        verbose_name = "author-book relation"
        verbose_name_plural = "author-book relations"

    def __str__(self):
        return f"{self.author} - {self.book}"