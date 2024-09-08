
from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from .models import Book
from .serializers import BookSerializer

class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    def create_book(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_created)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def list_books(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)




    def update_book(self, request):
        pass
    
    def delete_book(self, request):
        pass
# Create your views here.
