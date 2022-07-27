from django.shortcuts import get_object_or_404
from .models import Title, Flavor


def global_context(request):

    return {
        'titles': get_object_or_404(Title, pk=1),
    }