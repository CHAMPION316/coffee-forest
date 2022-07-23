from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to return the index page """
    
    return render(request, 'home/index.html')


# def flavor_view(request):
#     f = F.objects.all()

#     return render(request,"flavors/index.html", {'f',: f})
