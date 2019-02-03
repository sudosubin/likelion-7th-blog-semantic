from django.shortcuts import render, redirect
from .models import Photo


def home_view(request):
    photos = Photo.objects.all()
    context = {
        'photos': photos
    }
    return render(request, 'gallery/home.html', context)


def new_view(request):
    if (request.method == 'POST'):
        photo = Photo()
        photo.title = request.POST['title']
        photo.info = request.POST['info']
        photo.image = request.POST['image']
        photo.save()
        return redirect('/gallery/')
    return render(request, 'gallery/new.html')
