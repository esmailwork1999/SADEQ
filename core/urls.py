from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('advertising/', views.advertising, name='advertising'),
    path('architecture/', views.architecture, name='architecture'),
    path('fetch_pics/<str:type>',views.fetch_pics,name='fetch_pics')
]