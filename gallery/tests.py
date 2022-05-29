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
        
        
        
# image tests  

class ImageTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.category1 = Category(category_name = 'Nature')
        self.location1 = Location(location = 'Nairobi')
        self.category1.save_category()
        
        self.location1.save_location()
        
        
        
        self.image1 = Image(category= self.category1,location= self.location1,image ='test.jpg',description="test")
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image1, Image))
        
    # Testing Save Method
    def test_save_method(self):
        self.image1.save_image()
        image = Image.objects.all()
        self.assertTrue(len(image) > 0) 
        
     def test_updateImage(self):
    self.image.save_image()
    self.image.update_image(self.image.id, 'photos/test2.jpg')
    updated_image = Image.objects.get(id=self.image.id)
    self.assertEqual(updated_image.image, 'photos/test2.jpg')

  def test_deleteImage(self):
    self.image.save_image()
    self.image2 = Image.objects.create(image ='photos/test3.jpg', image_name = 'test3', image_desc= 'this is a test3', location_id=self.location, category_id=self.category)
    Image.delete_image(self.image.id)
    self.assertTrue(len(Image.objects.all())==1)
  
  def test_getImagesById(self):
    self.image.save_image()
    imagefound = Image.get_images_by_id(self.image.id)
    self.assertEqual(imagefound, self.image)
    
  def test_searchImage(self):
    self.category2 = Category.objects.create(category='Food')
    self.image2 = Image.objects.create(image ='photos/test3.jpg', image_name = 'test3', image_desc= 'this is a test3', location_id=self.location, category_id=self.category2)
    searchTerm = 'Food'
    self.image.save_image()
    searchResult = Image.search_image(searchTerm)
    self.assertEqual(searchResult.count(), 2)

  def test_filterlocation(self):
    self.image.save_image()
    self.location2 = Location.objects.create(location='Kisumu')
    self.image2 = Image.objects.create(image ='photos/test3.jpg', image_name = 'test3', image_desc= 'this is a test3', location_id=self.location2, category_id=self.category)
    filterlocationterm = 'Kisumu'
    searchResult = Image.filter_by_location(filterlocationterm)
    self.assertEqual(searchResult.count(), 1)                 
