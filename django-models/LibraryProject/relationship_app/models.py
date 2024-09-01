from django.db import models
class Author(models.Model):
    # Define the author model
    name = models.CharField(max_length=200)
    def __str__(self):
        #returns author name in a string representation
        return self.name
class Book(models.Model):
    #Define Book model
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name='books')
    def  __str__(self):
        #returns the book name in a string format
        return self.name
    
class Library(models.Model):
    #Define the Library model
    name = models.CharField(max_length=200)
    library = models.ManyToManyField(Boo'k')

    def __str__(self):
        #returns the string representation of the Library name
        return self.name
    
class Librarian(models.Model):
    #Define the librarian model
    name = models.CharField(max_length=255)
    library = models.OneToOneField(Library, on_delete= models.CASCADE, related_name='librarian')

    def __str__(self):
        #returns a string representation of the Librarian name
        return self.name



