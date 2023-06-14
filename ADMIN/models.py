from django.db import models

# Create your models here.
class itemtable(models.Model):
    itemname=models.CharField(max_length=25)
    itemprice=models.IntegerField()
    itemdescription=models.TextField()
    picture=models.FileField(upload_to="images")
    brand=models.CharField(max_length=25 )
    seller=models.CharField(max_length=25 )
    status=models.CharField(max_length=25 )
    colour=models.CharField(max_length=25 )
