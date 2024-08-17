CRUD OPERATIONS
from bookshelf.models import Book

Create Book
book = Book.objects.create(title="Hellis", author="James Newman",publication_year=2005)
output:
<Book: Book object (4)>

Retrieve Book
Book.objects.get(title="1984")

Update Book
book.title = “Nineteen Eighty-Four”
book.save()


Delete Book
book.delete()
output:

output:
(1, {'bookshelf.Book': 1})

