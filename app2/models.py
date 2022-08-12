from django.db import models

# Create your models here.
class CustomerData(models.Model):  #class Model is called from models (check package)
    username = models.CharField(max_length= 100)
    phone_no = models.BigIntegerField()
    dob = models.DateField()
    email = models.CharField(max_length= 100)
    product = models.CharField(max_length= 100)