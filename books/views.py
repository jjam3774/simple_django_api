from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from books.models import Book
from books.serializers import BookSerializer

# Decorater that declares the type of requests that the method will handle
@api_view(['GET', 'POST'])
def book_list(request, endpoint='mark'):
    if request.method == 'GET':
        url = 'https://learning.oreilly.com/api/v2/search/?query=author:\"{}\"'.format(
            endpoint)
        res = requests.get(url)
        output = json.loads(res.text)
        # print(json.dumps(output, indent=4, sort_keys=True))
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(output)
    # Handle the POST request and return status of POST
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, pk):
    try:
        book = book.objects.get(pk=pk)
    except book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def startpage(request):

    if request.method == 'GET':        
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
