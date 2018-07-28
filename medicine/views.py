from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Album


# def product(request):
#     all_albums =Album.objects.all()
#     #template = loader.get_template('medicine/product.html')
#     # context = {
#     #     'all_albums' : all_albums,
#     # }
#     return render (request,'medicine/product.html')
    #return render (request,'medicine/index.html', {'album' : all_albums })

def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("album not exist")
    return render (request,'medicine/detail.html', {'album' : album })
    #return HttpResponse("<h2>Details for Album id: "+str(album_id)+"</h2>")

def homePage(request):
    return render (request, 'medicine/homePage.html')

def product(request):
    return render (request, 'medicine/product.html')

def contact(request):
    return render (request, 'medicine/contact.html')
