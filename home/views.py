from django.shortcuts import render, redirect, reverse, get_object_or_404
from.models import Flavor

# Create your views here.

def index(request):
    """ A view to return the index page """
    flavors = Flavor.objects.filter().only('description_f')
    context = {
        'flavors': flavors
    }
    return render(request, 'home/index.html', context)


# def index(request):
#     """ A view to return the index page """
    
#     return render(request, 'home/index.html')
