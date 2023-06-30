from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('advertising/', views.advertising, name='advertising'),
    path('architecture/', views.architecture, name='architecture'),
]