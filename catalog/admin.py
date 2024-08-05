from django.contrib import admin
from .models import Author, Book, AuthorBook

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','date_of_birth')

class BookAdmin(admin.ModelAdmin):
    list_display = ('name','isbn','year')

class AuthorBookAdmin(admin.ModelAdmin):
    list_display = ('author','book')

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(AuthorBook, AuthorBookAdmin)