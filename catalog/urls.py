from django.urls import path
from .views import AuthorList, AuthorDetail, BookList, BookDetail, AuthorBookDetail, AuthorBookList
urlpatterns = [
    path('author/', AuthorList.as_view(), name='author'),
    path('author/<int:pk>/', AuthorDetail.as_view(), name='author-detail'),
    path('book/', BookList.as_view(), name='book'),
    path('book/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('author-book/', AuthorBookList.as_view(), name='author-book'),
    path('author-book/<int:pk>/', AuthorBookDetail.as_view(), name='author-book-detail'),
]