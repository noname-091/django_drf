from rest_framework import generics
from books.models import Book

from .serializer import BookSerializer
# Create your views here.

class BookApiView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
