from django.db import models

# Create your models here.
class GradeBook(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.CharField(max_length=10)
    # Add more fields as per your requirements