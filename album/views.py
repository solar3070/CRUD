from django.shortcuts import render, get_object_or_404, redirect
from .models import Album
from .form import AlbumPost

def album(request):
    images = Album.objects
    return render(request, 'album.html', {'images':images})

def imgdetail(request, image_id):
    details = get_object_or_404(Album, pk = image_id)
    return render(request, 'imgdetail.html', {'detail':details})

def albumpost(request):
    if request.method == 'POST':
        form = AlbumPost(request.POST, request.FILES)
        if form.is_valid():
            post=form.save()
            return redirect('album')
        else :
            return render(request, 'create.html', {'form': form})
    else:
        form = AlbumPost()
        return render(request, 'create.html', {'form':form})
