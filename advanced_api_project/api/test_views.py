from django.test import APITestCase
from .models import Book, Author
from .seriealizers import BookSerializer

class BookCreateTest(APITestCase):
    def setUp(self):
        self.author = Author.objects.create(name='Chimmamanda Ngozie')

    def test_create_book(self):
        data = {
            'title': 'Purple Hibiscus',
            'author': self.author,
            'publication_year': 2006
        }

        #Create New Book
        serializer = BookSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        book = serializer.save()

        #Verify Book Creation
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(book.title, data['title'])
        self.assertEqual(book.author.name, self.author.name)
        self.assertEqual(book.publication_year, data['publication_year'])