from django.db import models

# Create your models here.
class contact(models.Model):
    name = models.CharField( max_length=122, null=True)
    Email = models.CharField( max_length=122, null=True)
    phone =models.CharField( max_length=12, null=True)
    suggestion =models.TextField( null=True)  
    date =models.DateField( null=True)
    #jo dikhana h uske liye database  m object ka nam
    def __str__(self):
        return self.name
    