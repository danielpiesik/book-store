from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from utils.permissions import IsAdminUserOrReadOnly

from .models import Book
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_fields = ('authors', 'title', 'genre')
    permission_classes = (IsAuthenticated, IsAdminUserOrReadOnly)
