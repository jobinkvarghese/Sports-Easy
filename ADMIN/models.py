from django.db import models

# Create your models here.
class itemtable(models.Model):
    itemname=models.CharField(max_length=25)
    itemprice=models.IntegerField()
    itemdecription=models.TextField()
    picture=models.FileField(upload_to="images")