"""oauth_repos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.views.generic import TemplateView
from github_trending_repos import views

urlpatterns = [
    path('',TemplateView.as_view(template_name='start/start.html'), name='welcome'),
    path('admin/', admin.site.urls),
    path('home/', TemplateView.as_view(template_name='dashboard/home.html'), name='home'),
    path('accounts/', include('allauth.urls')),
    path('python/',views.PythonRepoView.as_view(),name='pythonrepo'),
    path('cprog/',views.CRepoView.as_view(),name='crepo'),
    path('cplusplus/',views.CplusplusRepoView.as_view(),name='cplusplusrepo'),
    path('java/',views.JavaRepoView.as_view(),name='javarepo'),
   
   ]
