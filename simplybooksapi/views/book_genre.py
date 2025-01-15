from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from simplybooksapi.models import BookGenre, Book, Genre


class BookGenreView(ViewSet):
  
    def retrieve(self, request, pk):
      try:
          bookGenre = BookGenre.objects.get(pk=pk)
          serializer = BookGenreSerializer(bookGenre)
          return Response(serializer.data)
      except BookGenre.DoesNotExist as ex:
          return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
      try:
        bookGenres = BookGenre.objects.all()
    
        serializer = BookGenreSerializer(bookGenres, many=True)
        return Response(serializer.data)
      except BookGenre.DoesNotExist as ex:
        return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
    def create(self, request):
      bookId = Book.objects.get(pk=request.data["book_id"])
      genreId = Genre.objects.get(pk=request.data["genre_id"])

      bookGenre = BookGenre.objects.create(
          book=bookId,
          genre=genreId,
      )
      serializer = BookGenreSerializer(bookGenre)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
      book = Book.objects.get(pk=request.data["book_id"])
      genre = Genre.objects.get(pk=request.data["genre_id"])
      
      bookGenre = BookGenre.objects.get(pk=pk)
      bookGenre.book = book
      bookGenre.genre= genre

      bookGenre.save()

      serializer = BookGenreSerializer(bookGenre)
      return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk):
      bookGenre = BookGenre.objects.get(pk=pk)
      bookGenre.delete()
      return Response(None, status=status.HTTP_204_NO_CONTENT)


class BookGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookGenre
        fields = ('id', 'book', 'genre' )
        depth = 2
