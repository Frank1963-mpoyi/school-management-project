from django.db import models

# Create your models here.
class Timetable(models.Model):
    # course = models.ForeignKey(Course, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    # Add more fields as per your requirements