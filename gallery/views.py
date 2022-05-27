from django.shortcuts import render

# Create your views here.

def gallery(request):
    
    return render(request, 'gallery/gallery.html')


def get_image_by_id(request,id):
    
    return render(request, 'gallery/gallery.html')
