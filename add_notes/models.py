from django.core import validators
from django.db import models 


# Create your models here.
class Notes(models.Model):
    name = models.CharField(max_length=50 , default="")
    note = models.TextField() 
    image = models.ImageField(upload_to = "images" , default="" , null=True ,) 

    def __str__(self):
        return self.name