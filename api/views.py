from rest_framework import generics
from books.models import Book

from .serializer import BookSerializer
# Create your views here.

class BookApiView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class AddBookApiView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class DeleteApiView(generics.DestroyAPIView):
    condition = {
    'author__icontains': 'John'  # Muallifning ismi "John" ni o'z ichiga olishi shart
    }
    queryset = Book.objects.filter(**condition)
    serializer_class = BookSerializer

