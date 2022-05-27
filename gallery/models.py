from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=80,null=False,blank=False)
    
    def __str__(self):
        return self.category_name
    
