from django.shortcuts import render, redirect
from blog.models import Blog
from blog.forms import BlogForm, CategoryForm
from django.contrib.auth.decorators import login_required



# Create your views here.
def view_all_blogs(request):
    blogs= Blog.objects.all().order_by('-date_posted')
    context= { 'blogs' :blogs}
    return render(request, 'blogs.html', context)

def view_a_blog(request, blog_id):
    blog= Blog.objects.get(id=blog_id)
    context = { 'blog' : blog}
    return render (request, 'blog.html', context)

def view_a_blog_byslug(request, slug_title):
    blog= Blog.objects.get(slug_title=slug_title)
    context = { 'blog' : blog}
    return render (request, 'blog.html', context)

@login_required
def view_delete_a_blog(request, blog_id):
    blog= Blog.objects.get(id=blog_id)
    if request.user!=blog.author:
        return redirect('view_all_blogs')
    blog.delete()
    return redirect('view_all_blogs')
@login_required 
def view_add_blog(request):
    form= BlogForm()
    if request.method == 'POST':
        form= BlogForm(request.POST, request.FILES)
        form.instance.author= request.user
        if(form.is_valid()):
            form.save()
            return redirect('view_all_blogs')
    context = {'form': form}
    return render(request, 'add_blog.html', context)

@login_required
def view_add_category(request):
    form= CategoryForm()
    
    if request.method == 'POST':
        form= CategoryForm(request.POST, request.FILES)
        if(form.is_valid()):
            form.save()
            return redirect('view_all_blogs')
    context = {'form' : form}
    return render(request, 'add_category.html', context)

@login_required
def view_update_blog(request, blog_id):
    blog= Blog.objects.get(id=blog_id)
    if request.user!=blog.author:
        return redirect('view_all_blogs')
    form= BlogForm(instance=blog)
    
    if request.method== 'POST':
        form= BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
        return redirect('view_all_blogs')
    return render(request, 'updates.html', {'form': form})
    