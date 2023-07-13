from django.db import models

# Create your models here.
class FinancialRecord(models.Model):
    # student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField()
    # Add more fields as per your requirements