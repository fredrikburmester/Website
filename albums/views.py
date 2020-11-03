import cv2
import os
import json
import glob
import time

from os import link
from .models import Album
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404, render
from fredrikburmester.settings import BASE_DIR
from django.views.decorators.http import require_GET

def album(request, album):
    album = album.title()

    # if 'Firefox' in request.META['HTTP_USER_AGENT'] or 'Chrome' in request.META['HTTP_USER_AGENT']:
    #     lazy = 'eager'
    # else:
    #     lazy = 'eager'

    found = False
    for obj in Album.objects.all():
        if album == obj.name.split(' ')[0]:
            album = get_object_or_404(Album, name=obj.name)
            found = True
            break

    if found == False: 
        response = redirect('/Home/')
        return response

    # if album in str(Album.objects.all()):
    #     album = get_object_or_404(Album, name=album)
    # else:
    #     return render(request, '404.html', {'album': album})
        
    def load_images_from_folder(album):
        album = album.split(' ')[0]
        images = []
        path = str(BASE_DIR) + '/static/images/' + album
        for img in glob.glob(path + '/*.jpg'):
            src = 'images/' + album + '/' + img.split('/')[-1]
            thumb = 'images/' + album + '/thumbs/' + img.split('/')[-1]

            data = {}
            index = img.split('/')[-1].split('.')[0]
            if len(index) == 1:
                index = '00' + index
            elif len(index) == 2:
                index = '0' + index

            data['index'] = index
            data['src'] = src
            data['thumb'] = thumb

            # if lazy == 'lazy':
            #     data['lazy_link'] = link
            
            images.append(data)
        return images

    obj = load_images_from_folder(album.name)
    obj = sorted(obj, key=lambda x : x['index'], reverse=True)

    if album.name == 'Home':
        album_name = 'My name is Fredrik Burmester'
    else: 
        album_name = album.name

    context = {
        'title': album.name,
        'albumName': album_name,
        'album': album,
        'images': obj
    }

    return render(request, 'index.html', context)

def error_404(request, exception):
    context = {}
    return render(request,'404.html', context)

@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow: /static/"
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")
