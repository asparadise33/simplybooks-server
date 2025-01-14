"""View module for handling requests for Books"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from simplybooksapi.models import Book, Author, Genre

class BookView(ViewSet):
    """Simply Books API Book view"""

    def retrieve(self, request, pk):
        """Handle GET requests for a single Book

        Returns:
            Response -- JSON serialized Book
        """
        try:
            book = Book.objects.get(pk=pk)
            genres = Genre.objects.filter(bookgenre__id=book.id)
            book.genres=genres
            serializer = BookGenreSerializer(book)
            return Response(serializer.data)
        except Book.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)


    def list(self, request):
        """Handle GET requests to get all Books

        Returns:
            Response -- JSON serialized list of Books
        """
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations for Book
      
        Returns:
            Response -- JSON serialized Book instance
        """
        author = Author.objects.get(pk=request.data["author_id"])

        book = Book.objects.create(
        title=request.data["title"],
        author=author,
        image=request.data["image"],
        price=request.data["price"],
        sale=request.data["sale"],
        description=request.data["description"],
        uid=request.data["uid"],
        )
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """Handle PUT requests for a Book

        Returns:
        Response -- Empty body with 204 status code
        """

        book = Book.objects.get(pk=pk)
        book.title=request.data["title"]
        author = Author.objects.get(pk=request.data["author_id"])
        book.author = author
        book.image=request.data["image"]
        book.price=request.data["price"]
        book.sale=request.data["sale"]
        book.description=request.data["description"]
        book.uid=request.data["uid"]
        book.save()
        serializer = BookSerializer(book)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk):
        book = Book.objects.get(pk=pk)
        book.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class BookSerializer(serializers.ModelSerializer):
    """JSON serializer for Books
    """
    class Meta:
        model = Book
        fields = ('id','author_id', 'title', 'image', 'price', 'sale', 'description', 'uid')
        depth = 1

class GenreSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Genre
    fields = ('id', 'genre_name')
class BookGenreSerializer(serializers.ModelSerializer):
    """JSON serializer for Books
    """
    genres = GenreSerializer(read_only=True, many=True)
    class Meta:
        model = Book
        fields = ('id','author_id', 'title', 'image', 'price', 'sale', 'description', 'uid', 'genres')
        depth = 1
