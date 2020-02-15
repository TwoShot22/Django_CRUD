from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog
from .forms import NewBlog

def welcome(request):
    return render(request, 'viewcrud/index.html')

def read(request):
    blogs = Blog.objects.all()
    return render(request, 'viewcrud/funccrud.html', {'blogs':blogs})

def create(request):
    # Save New Data to Blog == POST
    if request.method == 'POST':
        form = NewBlog(request.POST)

        # Allow Save
        if form.is_valid:
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')

    # Show 'newblog' page == GET
    else:
        # Show Form for Enter Content
        form = NewBlog()
        return render(request, 'viewcrud/new.html', {'form':form})

def update(request, pk):
    return

def delete(request, pk):
    blog = get_object_or_404(Blog, pk = pk)
    blog.delete()
    return redirect('home')