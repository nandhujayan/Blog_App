from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
     path('Addpost/', views.AddPost ,name="Addpost"),
     path('viewall/', views.viewAll ,name="viewall"),
 
  

]