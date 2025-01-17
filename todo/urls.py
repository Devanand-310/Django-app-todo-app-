from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('complete/<int:pk>/', views.complete_todo, name='complete_todo'),
    path('add/', views.add_todo, name= 'add_todo'),
    path('update/<int:pk>/', views.update_todo, name='update_todo'),
    path('delete/<int:pk>/', views.delete_todo, name='delete_todo'),
]