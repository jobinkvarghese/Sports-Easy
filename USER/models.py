from django.db import models

# Create your models here.
class regtable(models.Model):
    fname=models.CharField(max_length=25)
    lname=models.CharField(max_length=25)
    email=models.EmailField()
    address=models.TextField()
    State=models.CharField(max_length=25)
    pincode=models.IntegerField()
    DOB=models.DateField()
    gender=models.CharField(max_length=25)
    code=models.CharField(max_length=25)
    phoneno=models.IntegerField()
    password=models.CharField(max_length=25)
    confirmpassword=models.CharField(max_length=25)
