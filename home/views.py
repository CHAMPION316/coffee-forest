from django.shortcuts import render, redirect, reverse, get_object_or_404
from.models import Flavor, Title
from django import template

# Create your views here.

def index(request):
    """ A view to return the index page """
    flavors = Flavor.objects.order_by('description_f')[0:1].get()
    titles = Title.objects.order_by('title_f')[0:1].get()
    context = {
        'flavors': flavors,
        'titles': titles,
    }
    return render(request, 'home/index.html', context)
