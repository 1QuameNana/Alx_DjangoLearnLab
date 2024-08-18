from relationship_app.models import Book, Author
#Querry to search books by specific author
Author.objects.get(name=author_name), objects.filter(author=author)

books_by_author = Author.objects.filter(author=Author)


#Query to list all books ["Library.objects.get(name=library_name)", "books.all()"]
Library.objects.get(name=library_name), books.all()
books = Book.objects.all()
for book in books:
    print(book.title)


#Qery to retrieve Librarian
librarian = Librarain.objects.get(libray=library)
print(librarian.name)