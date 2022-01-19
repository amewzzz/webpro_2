from django.shortcuts import render, redirect

from accounts.forms import UserRegistrationForm


# Create your views here.

def view_user_register(request):
    if request.user.is_authenticated:
        return redirect('view_all_blogs')
    form= UserRegistrationForm()
    if request.method== "POST":
        form= UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context= {'form':form}
    return render(request, 'register.html', context)
