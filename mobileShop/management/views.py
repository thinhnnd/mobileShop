from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from management.models import MobilePhone, Branch

# Create your views here.

class PhoneListView(generic.ListView):
    model = MobilePhone 

def index(request):
    num_phones = MobilePhone.objects.all().count()
    num_branches = Branch.objects.all().count()
    top_ten_phones_list = MobilePhone.objects.all().order_by('-updated_at')[:10]
    context = {
        'num_phones': num_phones,
        'num_branches': num_branches,
        'top_ten_phones_list': top_ten_phones_list
    }
    return render(request, 'index.html', context = context)