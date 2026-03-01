from django.db import models

# Create your models here.
#this models.py store the data of user
class Student(models.Model):
    # id = models.AutoField()
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    address = models.TextField(null=True,blank=True)
    # image = models.ImageField()
    # file = models.FileField()
    # Date = models.DateField()
    
class Product(models.Model):
    # id = models.AutoField()
    price = models.IntegerField() 

class Car(models.Model):
    car_name = models.CharField(max_length=100)
    speed = models.IntegerField()
    def __str__(self) ->str:
        return self.car_name