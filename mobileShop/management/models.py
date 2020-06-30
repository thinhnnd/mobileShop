from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class MobilePhone(models.Model):
    title = models.CharField(max_length=200, unique=True, null=False, default="Tên Thiết bị", help_text="Enter a name of Product")
    price = models.PositiveIntegerField(null = True, blank = True, help_text="Enter price of product, min=10000")
    description = models.TextField(max_length=1000, null=True, blank=True)
    main_photo = models.ImageField(null = True, blank=True, upload_to='phones')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True) 
    firm = models.ForeignKey('Branch', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a particular phone instance."""
        return reverse('phone-detail', args=[str(self.id)])

#branch
class Branch(models.Model):
    title= models.CharField(
        max_length=30, 
        unique=True, 
        null=True, 
        help_text="Enter a firm name (e.g. SAMSUNG, iPhone, Huawei, etsc.)")
    description = models.TextField(max_length=1000, null=True)
    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a particular firm instance."""
        return reverse('firm-detail', args=[str(self.id)])
