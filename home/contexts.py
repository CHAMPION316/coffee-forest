"""
contexts for models in home/models.py
to allow for Admin use
"""
from django.shortcuts import get_object_or_404
from .models import Title, Icon


def global_context(request):
    """
    global context for model use
    """

    return {
        'titles': get_object_or_404(Title, pk=1),
        'icon_t': get_object_or_404(Icon, pk=1),
        'icon_f': get_object_or_404(Icon, pk=2),
        'icon_i': get_object_or_404(Icon, pk=3),
    }

def address_context(request):
    """
    context for address changes
    in Admin
    """
    business_location = 'https://www.google.com/maps/place/Caf%C3%A9+Pascal/@59.3421357,17.9861722,13z/data=!4m9!1m2!2m1!1scoffee+places+in+stockholm!3m5!1s0x465f77f743aac9cb:0xc16f1d3ee86dc04e!8m2!3d59.3421024!4d18.0519734!15sChpjb2ZmZWUgcGxhY2VzIGluIHN0b2NraG9sbVoVIhNjb2ZmZWUgaW4gc3RvY2tob2xtkgEEY2FmZZoBI0NoWkRTVWhOTUc5blMwVkpRMEZuU1VReU5rMTZhMHRCRUFF' #noqa
    business_email = 'coffeeforest@gmail.com'
    business_phone_number = '+46709664063'

    contexts = {
        'business_location': business_location,
        'business_email': business_email,
        'business_phone_number': business_phone_number,
    }

    return contexts
