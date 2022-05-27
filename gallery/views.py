from django.shortcuts import render
from .models import Category,Location,Image

# Create your views here.

def gallery(request):
    categories = Category.objects.all()
    images = Image.objects.all()
    
    dict = {'categories':categories,'images':images}
    
    return render(request, 'gallery/gallery.html',dict)


def get_image_by_id(request,id):
    image = Image.objects.get(id=id)
    
    
    
    return render(request, 'gallery/singlephoto.html',{'image':image})
