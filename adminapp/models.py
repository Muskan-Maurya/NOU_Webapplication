from django.db import models

# Create your models here.
class Material(models.Model):
    mid=models.AutoField(primary_key=True)
    program=models.CharField(max_length=50)
    branch=models.CharField(max_length=50)
    year=models.CharField(max_length=50)
    subject=models.CharField(max_length=50)
    materialtype=models.CharField(max_length=50)
    filename=models.CharField(max_length=500)
    myfile=models.FileField(upload_to='')
    posteddate=models.CharField(max_length=30)

class News(models.Model):
    nid=models.AutoField(primary_key=True)
    newstext=models.CharField(max_length=1000)
    posteddate=models.CharField(max_length=30)


    
