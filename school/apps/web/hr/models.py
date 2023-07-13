from django.db import models

# Create your models here.
class HR(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # Add more fields as per your requirements