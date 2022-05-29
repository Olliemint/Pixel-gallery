from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=80,null=False,blank=False)
    
    def __str__(self):
        return self.category_name
    
    def save_category(self):
        self.save()
        
    @classmethod
    def delete_category(cls, id):
        cls.objects.filter(id=id).delete()

    @classmethod
    def update_category(cls, id, cateUpdate):
        cls.objects.filter(id=id).update(category=cateUpdate)    
    
    
class Location(models.Model):
    location = models.CharField(max_length=80,null=False,blank=False)
    
    def __str__(self):
        return self.location
    
    def save_location(self):
        self.save()
        
    @classmethod
    def deleteLocation(cls, id):
        cls.objects.filter(id=id).delete()
        
    @classmethod
    def updateLocation(cls, id, locaUpdate):
        cls.objects.filter(id=id).update(location=locaUpdate)        
        
    
    
class Image(models.Model):
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL,null=True,blank=True)
    image = models.ImageField(null=False,blank=False)
    description = models.TextField(max_length=700,null=False,blank=False)
    
    def __str__(self):
        return self.description 
    
    
    def save_image(self):
        self.save()
        
    @classmethod
    def update_image(cls, id, imagechange):
        cls.objects.filter(id = id).update(image1 = imagechange)
        
    @classmethod
    def delete_image(cls, id):
        cls.objects.filter(id=id).delete()

    @classmethod
    def update_image(cls, id, imagechange):
        cls.objects.filter(id = id).update(image = imagechange)

    @classmethod
    def get_images_by_id(cls, id):
        try:
            image = cls.objects.get(id=id)
            return image
         
            
        
        except Image.DoesNotExist:
            print('Image does not exist')

    @classmethod
    def search_image(cls, category):
        images = Image.objects.filter(category__category_name=category)
        return images

    @classmethod
    def filter_by_location(cls, location):
        images = Image.objects.filter(location__location=location)
        return images      
        
      
    
