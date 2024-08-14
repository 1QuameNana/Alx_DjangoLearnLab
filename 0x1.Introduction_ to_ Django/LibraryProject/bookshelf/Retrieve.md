Instruction Retrieve and display all attributes of the book you just created.

from bookshelf.models import Book

Command:
Book.objects.get(title="1984")


output:
<Book: Book object (4)>
