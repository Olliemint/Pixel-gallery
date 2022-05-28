from django.urls import path
from . import views

urlpatterns =[
    path('',views.gallery, name='gallery'),
    path('photo/<str:id>/',views.get_image_by_id,name='single_photo'),
    path('',views.filter_by_location, name='loca'),
]