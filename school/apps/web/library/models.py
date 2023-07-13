from django.db import models

# Create your models here.
class Library(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    # Add more fields as per your requirements
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    # Add more fields as per your requirements