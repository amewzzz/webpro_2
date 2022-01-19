from socket import fromshare
from blog.models import Blog, Category
from django import forms #to import form function provided by django
from crispy_forms.helper import FormHelper

class BlogForm(forms.ModelForm): #creating form for blog model with django
    helper= FormHelper()
    class Meta:
        model=Blog
        fields= ['title', 'content', 'category', 'thumbnail' ] #including all fields from class Blog ->models.py
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields= '__all__'