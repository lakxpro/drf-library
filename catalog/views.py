from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS
from .models import Author,Book, AuthorBook

from .serializers import AuthorSerializer, BookSerializer, AuthorBookSerializer

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class AuthorList(generics.ListCreateAPIView):
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated|ReadOnly]

    def get_queryset(self):
        queryset = Author.objects.all()
        return queryset
    
class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]
    queryset = Author.objects.all()

class BookList(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated|ReadOnly]
    
    def get_queryset(self):
        queryset = Book.objects.all()
        if self.request.query_params.get('title__contains') :
            queryset = queryset.filter(name__contains=self.request.query_params.get('title__contains'))
        if self.request.query_params.get('printed__lte'):
            queryset = queryset.filter(year__lte=self.request.query_params.get('printed__lte'))
        return queryset

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    
class AuthorBookList(generics.ListCreateAPIView):
    serializer_class = AuthorBookSerializer
    permission_classes = [IsAuthenticated|ReadOnly]

    def get_queryset(self):
        queryset = AuthorBook.objects.all()
        return queryset
    
class AuthorBookDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AuthorBookSerializer
    permission_classes = [IsAuthenticated]
    queryset = AuthorBook.objects.all()
