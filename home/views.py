from django.shortcuts import render, redirect, reverse, get_object_or_404
from.models import Flavor, Title, History
from django import template

# Create your views here.

def index(request):
    """ A view to return the index page """
    flavors = Flavor.objects.order_by('description_f')[0:1].get()
    titles = Title.objects.order_by('title_f')[0:1].get()
    histories = History.objects.order_by('history_f')[0:1].get()
    histories2 = History.objects.order_by('history_f')[1:2].get()

    context = {
        'flavors': flavors,
        'titles': titles,
        'histories': histories,
        'histories2': histories2,
    }
    return render(request, 'home/index.html', context)
