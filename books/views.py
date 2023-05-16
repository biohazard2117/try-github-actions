from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics, viewsets, status
from rest_framework.response import Response


# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    
    def create(self, request):
             
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()
        serializer.save()

        return Response({"success": "Book created", "data": serializer.data}, status=status.HTTP_201_CREATED)
        
    def retrieve(self, request):
        # serializer_class = BookSerializer
        
        book_id = request.data["book_id"]
        # queryset = self.get_queryset()
        book = Book.objects.all()
        serializer = self.serializer_class(book, many = True)
        print(serializer.data)
        
        return Response({"success": "Book found", "data": serializer.data}, status=status.HTTP_200_OK)

