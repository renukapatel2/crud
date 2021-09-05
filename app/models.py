from django.db import models

# Create your models here.
class User(models.Model):
    fname = models.CharField(max_length=150,default="asd#45")
    lname = models.CharField(max_length=150,default="asd#45")
    email=models.EmailField(unique=True)
    pas = models.CharField(max_length=10)
    img = models.ImageField(upload_to="userimage/",default="xyz.jpg")
    
    def __str__(self):
        return self.name