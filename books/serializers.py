from rest_framework import serializers
from .models import Book, Author

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for Author model.

    Attributes:
    name (str): Name of the author.
    birth_year (int): Birth year of the author.

    """
    class Meta:
        model = Author
        fields = ['name', 'birth_year']
        

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for Book model.

    Attributes:
    title (str): Title of the book.
    isbn (str): ISBN-13 number of the book.
    published_year (int): Year when the book was published.
    author (Author): ForeignKey to Author model, representing the author of the book.

    """

    class Meta:
        model = Book
        fields = ['title', 'isbn', 'published_year', 'author']
    
    def validate_isbn(self, value):
        """
        Validate the format of the ISBN-13 number.

        Parameters:
        value (str): The ISBN-13 number to validate.

        Returns:
        str: The validated ISBN-13 number.

        Raises:
        serializers.ValidationError: If the ISBN-13 number is not exactly 13 characters long.

        """
        if len(value) != 13:
            raise serializers.ValidationError("ISBN must be 13 characters long.")
        return value
