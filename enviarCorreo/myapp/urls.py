from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),  
    path('mail/', views.correo),  
#    path('about/', views.about), 
 #   path('hello/<str:username>', views.hello),
 #   path('mail/', views.correo, name="mail"),
 #   path('', views.index, name='index')
 #   path('mail/', views.correo),
 #   path('', views.index)
]