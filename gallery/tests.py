from unicodedata import category
from django.test import TestCase

from .models import Location,Category,Image

# Create your tests here.

# Category tests
class CategoryTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.category1 = Category(category_name = 'Nature')
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.category1, Category))
        
    # Testing Save Method
    def test_save_method(self):
        self.category1.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)
        
    def test_deleteCategory(self):
        self.category.save_category()
        self.category2 = Category.objects.create(category='Travel')
        Category.deleteCategory(self.category2.id)
        self.assertTrue(len(Category.objects.all())==1)     
    
    
    def test_updateCategory(self):
        update_term = 'Nature'
        self.category.saveCategory()
        Category.updateCategory(self.category.id, update_term)  
        updated_one = Category.objects.get(id=self.category.id)
        self.assertEqual(updated_one.category, 'Nature')

# location tests

class LocationTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.location1 = Location(location = 'Nairobi')
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.location1, Location))
        
    # Testing Save Method
    def test_save_method(self):
        self.location1.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location) > 0) 
        
        
    def test_deleteLocation(self):
        self.location.saveLocation()
        self.location2 = Location.objects.create(location='Nakuru')
        Location.deleteLocation(self.location2.id)
        self.assertTrue(len(Location.objects.all())==1) 
        
        
    def test_updateLocation(self):
        update_term = 'Eldoret'
        self.location.saveLocation()
        Location.updateLocation(self.location.id, update_term)  
        updated_one = Location.objects.get(id=self.location.id)
        self.assertEqual(updated_one.location, 'Eldoret')        
        
        
        
# image tests  

class ImageTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.category1 = Category(category_name = 'Nature')
        self.location1 = Location(location = 'Nairobi')
        self.category1.save_category()
        
        self.location1.save_location()
        
        
        
        self.image1 = Image(category= self.category1,location= self.location1,image ='nature.jpg',description="nature image")
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image1, Image))
        
    # Testing Save Method
    def test_save_method(self):
        self.image1.save_image()
        image = Image.objects.all()
        self.assertTrue(len(image) > 0) 
        
    
    def test_updateImage(self):
        self.image1.save_image()
        self.image1.update_image(self.image1.id, 'food.jpg')
        updated_image = Image.objects.get(id=self.image1.id)
        self.assertEqual(updated_image.image1, 'food.jpg') 
        
    def test_deleteImage(self):
        self.image.save_image()
        self.image2 = Image.objects.create(category= self.category1,location= self.location1,image ='flower.jpg',description="flower image")
        Image.delete_image(self.image.id)
        self.assertTrue(len(Image.objects.all())==1) 
        
        
    def test_search_image(self):
        self.category2 = Category.objects.create(category='Food')
        self.image2 = Image.objects.create(category= self.category1,location= self.location1,image ='flower.jpg',description="flower image")
        searchTerm = 'Flower'
        self.image.save_image()
        search_result = Image.search_image(searchTerm)
        self.assertEqual(search_result.count(), 2)
        
    def test_filterlocation(self):
        self.image.save_image()
        self.location2 = Location.objects.create(location='Nakuru')
        self.image2 = Image.objects.create(category= self.category1,location= self.location1,image ='flower.jpg',description="flower image")
        filterlocationterm = 'Nakuru'
        search_result = Image.filter_by_location(filterlocationterm)
        self.assertEqual(search_result.count(), 1)                      
