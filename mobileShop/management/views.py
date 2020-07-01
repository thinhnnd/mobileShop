from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from management.models import Phone, Branch

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from management.forms import EditPhoneForm
from django.conf import settings
import os 

# Create your views here.

class PhoneListView(generic.ListView):
    #template_name = 'products/phone-detail.html'
    model =Phone
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(*kwargs)
        context['phone'] = self.object
        return context   

class PhoneDetailView(generic.DetailView):
    template_name = 'products/phone-detail.html'
    model =Phone

def index(request):
    num_phones =Phone.objects.all().count()
    branches = Branch.objects.all()
    top_ten_phones_list =Phone.objects.all().order_by('-created_at')[:10]
    context = {
        'num_phones': num_phones,
        'num_branches': branches.count(),
        'top_ten_phones_list': top_ten_phones_list
    }
    return render(request, 'index.html', context = context)

def delete_phone(request, id):
    phone = get_object_or_404(Phone, pk=id)
    if(request.method == 'DELETE'):
        print('delete successfully')
    return HttpResponseRedirect('/')

def edit_phone(request, id):
    phone = get_object_or_404(Phone, pk=id)
    context = {
        'phone': phone,
    }

    if request.method == 'POST':

        # get data from FORM POST
        formData =request.POST
        new_title = formData.get('title', '')
        new_description = formData.get('description', '')
        new_price = formData.get('price', '')
        new_main_photo = request.FILES.get('main_photo', False)
        remove_old_image = formData.get('remove_old_image', False)

        # GET object from databases
        updated_phone =Phone.objects.get(pk=id)
       
        updated_phone.price = new_price
        updated_phone.description = new_description
        updated_phone.title = new_title

        # Check if filepath exist to save image
        if new_main_photo != False:
            #check is remove old image = true
            if remove_old_image == "on":
                print(f'remove_old_image: {remove_old_image}') 
                os.remove(f'{settings.MEDIA_ROOT}/{updated_phone.main_photo.name}')
            updated_phone.main_photo = request.FILES['main_photo']



        updated_phone.save()
        print(f'new_main_photo: {new_main_photo}')
        print(f'new_price: {new_price}')
        print(f'new_description: {new_description}')
        print(f'new_title: {new_title}') 
        print(f'remove_old_image: {remove_old_image}') 
        context = {
            'phone': updated_phone,
            'message': 'Successfully updated'
        }    
        return render(request, 'products/product-edit.html', context = context )

    if request.method == 'DELETE':
        print('delete')

    return render(request, 'products/product-edit.html', context=context)

    def handle_uploaded_file(f):
        with open('media/phone/' + f, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)