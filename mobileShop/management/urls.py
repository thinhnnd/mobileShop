from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('phone/<int:id>/edit', views.edit_phone, name='edit'),
] 