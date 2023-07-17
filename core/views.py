from django.db.models import Q
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .models import Category, Picture
from .utils import filter_pictures

# Create your views here.
def home(request):
    return render(request, 'site/home.html')




def architecture(request):
    return filter_pictures(request, '1', 'site/architecture.html')
def fetch_pics(request,type):
    if request.method == "GET":
        pictures = Picture.objects.filter(type=type)
        title_filter = request.GET.get('title')
        category_filter = request.GET.get('category')
        if title_filter and category_filter:
            pictures = pictures.filter(Q(title__icontains=title_filter) & Q(category__id=category_filter))
        elif title_filter:
            pictures = pictures.filter(title__icontains=title_filter)
        elif category_filter:
            pictures = pictures.filter(category__id=category_filter)
        pictures_data = {}
        for i, picture in enumerate(pictures):
            picture_data = {
                'title': picture.title,
                'image_url': picture.image.url,
            }
            pictures_data[i] = picture_data
    return JsonResponse({"pictures":pictures_data},safe=False)

def advertising(request):
    return filter_pictures(request, '2', 'site/advertising.html')