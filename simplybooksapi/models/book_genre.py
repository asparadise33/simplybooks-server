from django.db import models
from .genre import Genre
from .book import Book

class BookGenre(models.Model):
  genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name="bookgenre")
  book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="genrebook")
