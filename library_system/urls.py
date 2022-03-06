"""library_system URL Configuration

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
from django.urls import path,include
from bookmanagement.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', homepage, name = "homepage"),
    path('', homepage, name = "homepage"),
    path('show-all-books/', show_all_books, name = "show_all_books"),
    path('show_active_books/', show_active_books, name = "show_active_books"),
    path('show_inactive_books/', show_inactive_books, name = "show_inactive_books"),
    path('edit/<int:id>/', edit_data, name = "edit_data"),
    path('delete/<int:id>/', delete_book, name = "delete_book"),
    path('soft_delete/<int:id>/', soft_delete_book, name = "soft_delete_or_reco_book"),
    
]
    # path('__debug__/', include('debug_toolbar.urls')),

# show_active_books