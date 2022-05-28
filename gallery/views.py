
from django.shortcuts import render,redirect
from .models import Category,Location,Image
from django.contrib import messages

# Create your views here.

def gallery(request):
    locations = Location.objects.all()
    categories = Category.objects.all()
    
    # filter by location
    if request.GET.get('location'):
        images = Image.objects.filter(location__location=request.GET.get('location'))
        return render(request, 'gallery/gallery.html', {'images':images,'categories':categories,'locations':locations})
    
    # filter by category
    category = request.GET.get('category')
    if category is None:
        images = Image.objects.all()
    
    else:
        images = Image.objects.filter(category__category_name=category)
        
        
    
    
    
    # dictionary for  all data
    dict = {'categories':categories,'images':images,'locations':locations}
    
    return render(request, 'gallery/gallery.html',dict)


def get_image_by_id(request,id):
    image = Image.objects.get(id=id)
    
    
    
    return render(request, 'gallery/singlephoto.html',{'image':image})


def filter_by_location(request,location):
   
    images = Image.objects.get(location=location)
 
    
    return render(request, 'gallery/photolocation.html',{'images':images})


def search_image(request):
    if 'search' in request.GET and request.GET['search']:
        
        search_term  = request.GET.get('search')
        term = search_term.capitalize()
        searchresults = Image.objects.filter(category__category_name=term)
        
       
        return render(request, 'gallery/category_search.html', {'searchresults': searchresults})
        

    else:
        return redirect('gallery')
        
    
    
     
    
