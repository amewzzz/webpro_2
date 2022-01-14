from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    
    name= models.CharField(max_length=20)
    def __str__ (self):
        return self.name
    
class Blog(models.Model):
    title=models.CharField(max_length=50)
    body= models.TextField()
    date_posted= models.DateTimeField(auto_now_add=True)
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    category= models.ForeignKey (Category, on_delete= models.CASCADE)
    thumbnail= models.ImageField (upload_to= 'blog/', blank=True, null=True)
    
    def __str__(self):
        return self.title 
    

    
    
