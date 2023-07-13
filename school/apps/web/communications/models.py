from django.db import models

# Create your models here.

class Communication(models.Model):
    sender = models.ForeignKey(Staff, on_delete=models.CASCADE)
    recipient = models.ForeignKey(Student, on_delete=models.CASCADE)
    message = models.TextField()
    sent_date = models.DateTimeField(auto_now_add=True)
    # Add more fields as per your requirements