"""View module for handling requests for artists"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from simplybooksapi.models import Author

class AuthorView(ViewSet):
    """Simply Books API Author view"""

    def retrieve(self, request, pk):
        """Handle GET requests for a single Author

        Returns:
            Response -- JSON serialized Author
        """
        try:
            author = Author.objects.get(pk=pk)
            serializer = AuthorSerializer(author)
            return Response(serializer.data)
        except Author.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)


    def list(self, request):
        """Handle GET requests to get all Authors

        Returns:
            Response -- JSON serialized list of Authors
        """
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations for Author
      
        Returns:
            Response -- JSON serialized Author instance
        """

        author = Author.objects.create(
        first_name=request.data["first_name"],
        last_name=request.data["last_name"],
        email=request.data["email"],
        image=request.data["image"],
        favorite=request.data["favorite"],
        uid=request.data["uid"],
        )
        serializer = AuthorSerializer(author)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """Handle PUT requests for an author

        Returns:
        Response -- Empty body with 204 status code
        """

        author = Author.objects.get(pk=pk)
        author.first_name=request.data["first_name"]
        author.last_name=request.data["last_name"]
        author.email=request.data["email"]
        author.image=request.data["image"]
        author.favorite=request.data["favorite"]
        author.uid=request.data["uid"]
        author.save()
        serializer = AuthorSerializer(author)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk):
        author = Author.objects.get(pk=pk)
        author.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class AuthorSerializer(serializers.ModelSerializer):
    """JSON serializer for Authors
    """
    class Meta:
        model = Author
        fields = ('email', 'first_name', 'last_name', 'image', 'favorite', 'uid')
        depth = 1
