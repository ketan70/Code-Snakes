"""test_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from . import views

urlpatterns = [
    ## Do not put a space between the path, like this: "_", as it can cause errors in the application. Have you thought about what the error might be?
    path('form', views.form),  

    # show the data  
    path('show/',views.show),
 
    # call edit whith id
    path('edit/<int:id>', views.edit), 

    # update with id 
    path('update/<int:id>', views.update),  

    # delete with id
    path('delete/<int:id>', views.destroy), 

    # common admin call
    path('admin/', admin.site.urls),
]
