from django import forms

from .models import Phone

class EditPhoneForm(forms.Form):
    title = forms.CharField(label='Your name', max_length=100)
    price = forms.CharField()
    description = forms.Textarea()
    price = forms.FileField()

    class Meta:
        model =Phone
        fields = ('title', 'description', 'main_photo', 'firm', 'price')