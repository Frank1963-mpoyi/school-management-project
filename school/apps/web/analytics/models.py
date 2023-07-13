from django.db import models

# Create your models here.
class Analytics(models.Model):
    # student = models.ForeignKey(Student, on_delete=models.CASCADE)
    # course = models.ForeignKey(Course, on_delete=models.CASCADE)
    marks = models.DecimalField(max_digits=5, decimal_places=2)
    # Add more fields as per your requirements