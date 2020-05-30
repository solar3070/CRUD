from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
from .form import BlogPost

def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs':blogs})

def txtdetail(request, blog_id):
    details = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'txtdetail.html', {'detail':details})

def blogpost(request):
    if request.method == 'POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    else:
        form = BlogPost()
        return render(request, 'new.html', {'form':form})

def update(request, pk):
    blog = get_object_or_404(Blog, pk = pk)
    form = BlogPost(request.POST, instance=blog)
    if form.is_valid(): 
        form.save() 
        return redirect('home')
    return render(request, 'new.html', {'form':form})

def delete(request, pk):
    blog = get_object_or_404(Blog, pk =pk)
    blog.delete()
    return redirect('home')