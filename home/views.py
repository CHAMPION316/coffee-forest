from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Flavor

# Create your views here.

def index(request):
    """ A view to return the index page """
    
    return render(request, 'home/index.html')


def flavor_description(request, flavor_id):
    """ A view to show individual product details """

    flavor = get_object_or_404(Flavor, pk=flavor_id)

    context = {
        'flavor': flavor,
    }
    
    return render(request, 'home/flavors.html', context)


# def flavor_view(request):
#     f = F.objects.all()

#     return render(request, "home/components/flavors.html", {'f': f})