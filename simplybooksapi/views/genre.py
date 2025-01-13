"""View module for handling requests for Genres"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from simplybooksapi.models import Genre

class GenreView(ViewSet):
    """Simply Books API Genre view"""

    def retrieve(self, request, pk):
        """Handle GET requests for a single Genre

        Returns:
            Response -- JSON serialized Genre
        """
        try:
            genre = Genre.objects.get(pk=pk)
            serializer = GenreSerializer(genre)
            return Response(serializer.data)
        except Genre.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)


    def list(self, request):
        """Handle GET requests to get all Genres

        Returns:
            Response -- JSON serialized list of Genres
        """
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations for Genre
      
        Returns:
            Response -- JSON serialized genre instance
        """
        genre = Genre.objects.create(
        genre_name=request.data["genre_name"],
        )
        serializer = GenreSerializer(genre)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """Handle PUT requests for a Genre

        Returns:
        Response -- Empty body with 204 status code
        """

        genre = Genre.objects.get(pk=pk)
        genre.genre_name=request.data["genre_name"]
        genre.save()
        serializer = GenreSerializer(genre)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk):
        genre = Genre.objects.get(pk=pk)
        genre.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class GenreSerializer(serializers.ModelSerializer):
    """JSON serializer for Genres
    """
    class Meta:
        model = Genre
        fields = ('id','genre_name')
        depth = 1
