from django.shortcuts import render
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import books,students
from. serializers import BookSerializer, StudentSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
import re

class StudentAPI(APIView):
    def get(self, request):
        students_object = students.objects.all()
        serializer = StudentSerializer(students_object, many=True)
        return Response({'status':200, 'payload': serializer.data})

    def post(self, request):
        data = request.data
        pattern = r'^[0-9]+$'
        if not re.fullmatch(pattern, data['age']):
            return Response({'status':403, 'message': 'isbn must be numeric'})
        serializer = StudentSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status':403, 'errors':serializer.errors, 'message': 'Some thing went wrong'})
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request):
        try:
            student_obj = students.objects.get(id=request.data['id'])
            serializer = StudentSerializer(student_obj, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)       
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({'status':403, 'message':'invalid_id'})

    def patch(self, request):
        try:
            student_obj = students.objects.get(id=request.data['id'])
            serializer = StudentSerializer(student_obj, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)       
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({'status':403, 'message':'invalid_id'})       
    
    def delete(self, request):
        try:
            id = request.GET.get('id')
            student_obj = students.objects.get(id=id)
            student_obj.delete()
            return Response({'status': 403, 'message':'Deleted'})
        except Exception as e:
            print(e)
            return Response({'status':403, 'message':'invalid_id'})

# class BookCreateListView(generics.ListCreateAPIView):
#     queryset = books.objects.all()
#     serializer_class = BookSerializer
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
#     filterset_fields = ['author', 'published_date']  # exact match
#     search_fields = ['title', 'author']              # partial match
#     ordering_fields = ['title', 'published_date']

# class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = books.objects.all()
#     serializer_class = BookSerializer

from rest_framework.decorators import api_view
from rest_framework.response import  Response
from rest_framework import status
import re

@api_view(['GET', 'POST'])
def book_list_create(request):
    if request.method == 'GET':
        books_object = books.objects.all()
        serializer = BookSerializer(books_object, many=True)
        return Response({'status':200, 'payload': serializer.data})
    if request.method == 'POST':
        data = request.data
        pattern = r'^[0-9]+$'
        if not re.fullmatch(pattern, data['isbn']):
            return Response({'status':403, 'message': 'isbn must be numeric'})
        serializer = BookSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status':403, 'errors':serializer.errors, 'message': 'Some thing went wrong'})
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def book_detail(request, pk):
    try:
        book = books.objects.get(pk=pk)
    except books.DoesNotExist:
        return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)       
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PATCH':
        serializer = BookSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)       
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)