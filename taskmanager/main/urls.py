from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('create', views.create, name='create'),
    path('cat_page', views.cat_page, name='cat_page'),
    path('dog_page', views.dog_page, name='dog_page'),
]
