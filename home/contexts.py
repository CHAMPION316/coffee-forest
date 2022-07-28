from django.shortcuts import get_object_or_404
from .models import Title, Flavor, History


def global_context(request):

    return {
        'titles': get_object_or_404(Title, pk=1),
        'flavors': get_object_or_404(Flavor),
        'histories': get_object_or_404(History, pk=1),
        'histories2': get_object_or_404(History, pk=2),
    }
