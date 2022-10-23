"""
views.py in home app that allows
all models in app to be viewable
on webpage
"""
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Flavor, Title, History, Icon
from django import template

from django.core.mail import send_mail
from django.contrib import messages


def index(request):
    """ A view to return the index page """


    flavors = Flavor.objects.all()
    titles = Title.objects.order_by('title_f')[0:1].get()
    histories = History.objects.all()
    icon_t = Icon.objects.order_by('website')[0:1].get()
    icon_f = Icon.objects.order_by('website')[1:2].get()
    icon_i = Icon.objects.order_by('website')[2:3].get()

    context = {
        'flavors': flavors,
        'titles': titles,
        'histories': histories,
        'icon_t': icon_t,
    }

    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_message = request.POST['message']

        name = message_name.strip()
        message = message_message.strip()

        if not message:
            saved_name = name
            saved_email = message_email

            messages.error(
                request,
                'Please include a message so we can help.'
                )
            return render(request, 'home/index.html', {
                'saved_name': saved_name,
                'saved_email': saved_email,
            })

        elif not name:
            saved_email = message_email
            saved_message = message

            messages.error(
                request,
                'Please include your name.'
                )
            return render(request, 'home/index.html', {
                'saved_message': saved_message,
                'saved_email': saved_email,
            })

        else:
            send_mail(
                f'Message from {name}',
                message_message,
                message_email,
                ['royer.seguracalderon@gmail.com', ],
                )

        return render(request, 'home/index.html', {
            'name': name,
        })

    else:
        return render(request, 'home/index.html', context)
