
from django.urls import path
from . import views

urlpatterns = [  
    path('',views.Home,name='home'),
    path('delete/<int:roll>',views.delete, name='delete'),
    path('add_teacher/',views.add_teacher, name = "add_teacher"),
]