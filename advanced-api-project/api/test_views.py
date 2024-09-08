from django.test import APITestCase
from .models import Book, Author
from .serializers import BookSerializer
from rest_framework import status 
from rest_framework import response.data
from django.contrib.auth.models import User

class BookCreateTest(APITestCase):
    def setUp(self):
        self.username = 'testUser'
        self.password ='testtpas2009'
        self.user = User.objects.create_user(username=self.name, password=self.password)
        self.client.login(username=self.username, password=self.password)



    def setUp(self):
        self.author = Author.objects.create(name='Nacee')

    def test_create_book(self):
        data = {
            'title': 'Onaapo',
            'author': self.author,
            'publication_year': 2020
        }

    
        #Create a Book
        serializer = BookSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        book = serializer.save()

        #Verify Book Creation
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(book.title, data['title'])
        self.assertEqual(book.author.name, self.author.name)
        self.assertEqual(book.publication_year, data['publication_year'])