from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('phone/<int:pk>', views.PhoneDetailView.as_view(), name='phone-detail'),
    path('phone/<int:id>/edit', views.edit_phone, name='edit'),
    path('phone/<int:id>/delete', views.delete_phone, name='delete'),
] 