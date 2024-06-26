from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator
import datetime
from .validators import validate_isbn13, validate_alpha  # Import custom validators

current_year = datetime.date.today().year

class Author(models.Model):
    """
    Model representing an author.

    Attributes:
    name (str): Name of the author. Only alphabetic characters and spaces allowed.
    birth_year (int): Birth year of the author, validated to be at least 1900.
    """

    name = models.CharField(max_length=100, validators=[validate_alpha])
    birth_year = models.IntegerField(validators=[
        MinValueValidator(1900, message=f"Humans don't live that long anymore budd."),
        MaxValueValidator(current_year-6, message=f"At least a six years old person please.")])

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Model representing a book.

    Attributes:
    title (str): Title of the book.
    isbn (str): ISBN-13 number of the book, must be 13 digits long and pass checksum validation.
    published_year (int): Year when the book was published, validated to be between 1000 and the current year.
    author (Author): ForeignKey to Author model, representing the author of the book.
    """

    title = models.CharField(max_length=200)
    isbn = models.CharField(
        max_length=13,
        unique=True,
        validators=[
            MinLengthValidator(13, message='ISBN must be 13 digits long.'),
            validate_isbn13  # Custom validator for ISBN-13 format and checksum
        ]
    )
    published_year = models.IntegerField(
        validators=[
            MaxValueValidator(current_year),
            MinValueValidator(1000)
        ]
    )
    author = models.ForeignKey(
        Author,
        related_name='books',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title