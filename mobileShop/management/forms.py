from django import forms

from .models import MobilePhone

class EditPhoneForm(forms.Form):
    title = forms.CharField(label='Your name', max_length=100)
    price = forms.CharField()
    description = forms.Textarea()
    price = forms.FileField()

    class Meta:
        model = MobilePhone
        fields = ('title', 'description', 'main_photo', 'firm', 'price')