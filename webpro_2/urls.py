"""webpro_2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from blog.views import view_all_blogs, view_a_blog, view_delete_a_blog, view_add_blog, view_add_category

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogs/', view_all_blogs, name= 'view_all_blogs' ),
    path('blogs/add/', view_add_blog, name= 'view_add_blog' ),
    path('blogs/category/add', view_add_category, name= 'view_add_category' ),
    path('blogs/<int:blog_id>', view_a_blog, name= 'view_a_blog'),
    path('blogs/delete/<int:blog_id>', view_delete_a_blog, name= 'view_delete_a_blog'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
