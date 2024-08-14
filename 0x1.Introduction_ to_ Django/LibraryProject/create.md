"""Instruction Create a Book instance with the title “1984”, author “George Orwell”, and publication year 1949
from bookshelf.models import Book"""

from bookshelf.models import Book

command:

book.objects.create(title="1984", author="George Orwell",publication_year=1949)

output: <Book: Book object (4)>
