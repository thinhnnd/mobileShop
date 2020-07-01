from django.conf import settings
from .models import Phone, Branch

def management(request):
    branches = Branch.objects.all()
    kwargs = {
        'branches': branches,
    }
    return kwargs