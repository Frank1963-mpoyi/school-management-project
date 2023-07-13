from django.db import models

# Create your models here.
class Parent(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # Add more fields as per your requirements

class ParentStudentRelation(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    # student = models.ForeignKey(Student, on_delete=models.CASCADE)
    # Add more fields as per your requirements