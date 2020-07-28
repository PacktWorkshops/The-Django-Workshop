from django.db import models

class Book(models.Model):
    '''A model that stores the catalog of the books we know about.

    The model is used for storing the records of the books we know about
    by maintaining the details of the name of the book and the author who
    has written the book.
    '''
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=50)