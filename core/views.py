from django.shortcuts import render
from .utils import filter_pictures

# Create your views here.
def home(request):
    return render(request, 'site/home.html')




def architecture(request):
    return filter_pictures(request, '1', 'site/architecture.html')


def advertising(request):
    return filter_pictures(request, '2', 'site/advertising.html')