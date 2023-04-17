from django.db import models

# Create your models here.
class Post(models.Model):

    CH1=((1,'Aerobic Fitness'),(2,'FullBody Fitness'),(3,'Flexible Fitness'))
    CH2=((0,'Inactive'),(1,'Active'))
    fullname=models.CharField(max_length=50,verbose_name="User Name")
    age=models.IntegerField(verbose_name="User Age")
    gender=models.CharField(max_length=500,verbose_name="User Gender")
    weight=models.IntegerField(verbose_name="User Weight")
    cat=models.IntegerField(choices=CH1,verbose_name="Category")
    status=models.IntegerField(choices=CH2,verbose_name="Status")
    created_on=models.DateTimeField(verbose_name="Date of creation")
    uid=models.IntegerField()

    def __str__(self):
        return self.fullname

class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    Status=models.BooleanField()

class Contact(models.Model):
    #sno=models.AutoField(Primary_key=True)
    name=models.CharField(max_length=255)
    phone=models.CharField(max_length=13)
    email=models.CharField(max_length=100)
    content=models.TextField()
    timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

