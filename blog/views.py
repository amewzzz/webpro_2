from django.shortcuts import render, redirect
from blog.models import Blog
from blog.forms import BlogForm, CategoryForm



# Create your views here.
def view_all_blogs(request):
    blogs= Blog.objects.all()
    context= { 'blogs' :blogs}
    return render(request, 'blogs.html', context)

def view_a_blog(request, blog_id):
    blog= Blog.objects.get(id=blog_id)
    context = { 'blog' : blog}
    return render (request, 'blog.html', context)


def view_delete_a_blog(request, blog_id):
    blog= Blog.objects.get(id=blog_id)
    blog.delete()
    return redirect('view_all_blogs')

def view_add_blog(request):
    form= BlogForm()
    if request.method == 'POST':
        form= BlogForm(request.POST, request.FILES)
        if(form.is_valid()):
            form.save()
            return redirect('view_all_blogs')
    context = {'form': form}
    return render(request, 'add_blog.html', context)

def view_add_category(request):
    form= CategoryForm()
    if request.method == 'POST':
        form= CategoryForm(request.POST, request.FILES)
        if(form.is_valid()):
            form.save()
            return redirect('view_all_blogs')
    context = {'form' : form}
    return render(request, 'add_category.html', context)