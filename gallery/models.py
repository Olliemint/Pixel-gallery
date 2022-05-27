from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=80,null=False,blank=False)
    
    def __str__(self):
        return self.category_name
    
    
class Location(models.Model):
    location = models.CharField(max_length=80,null=False,blank=False)
    
    def __str__(self):
        return self.location
    
    
class Image(models.Model):
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL,null=True,blank=True)
    name = models.CharField(max_length=80,null=False,blank=False)
    description = models.TextField(max_length=700,null=False,blank=False)
    
    def __str__(self):
        return self.description   
    
