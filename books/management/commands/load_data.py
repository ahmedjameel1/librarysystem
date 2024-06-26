import csv
from django.core.management.base import BaseCommand
from books.models import Author, Book

class Command(BaseCommand):
    help = 'Load data from CSV files'

    def handle(self, *args, **kwargs):
        self.load_authors()
        self.load_books()

    def load_authors(self):
        file_path = 'books/helpers/authors.csv'
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Author.objects.update_or_create(
                    name=row['name'],
                    defaults={'birth_year': row['birth_year']}
                )
        self.stdout.write(self.style.SUCCESS('Authors loaded successfully'))

    def load_books(self):
        file_path = 'books/helpers/books.csv'
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                author = Author.objects.get(id=row['author'])
                Book.objects.update_or_create(
                    title=row['title'],
                    defaults={
                        'isbn': row['isbn'],
                        'published_year': row['published_year'],
                        'author': author
                    }
                )
        self.stdout.write(self.style.SUCCESS('Books loaded successfully'))
