from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    # Add more fields as per your requirements
    
class StudentPortal(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    # Add more fields as per your requirements
    
class Report(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    # course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.CharField(max_length=10)
    # Add more fields as per your requirements