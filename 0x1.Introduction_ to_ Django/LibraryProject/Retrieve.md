Retrieve Book

from bookshelf.modesls import Book
""" Instruction to retrieve and display existing instances of Book
"""
Command:

Book.objects.get(title="1984")

output:
<Book: Book object (4)>


