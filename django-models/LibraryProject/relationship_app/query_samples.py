from relationship_app.models import Book, Author
#Querry to search books by specific author
books_by_author = Book.objects.filter(author=Author)


#Query to list all books
books = Book.objects.all()
for book in books:
    print(book.title)


#Qery to retrieve Librarian
librarian = Librarain.objects.get(libray=library)
print(librarian.name)