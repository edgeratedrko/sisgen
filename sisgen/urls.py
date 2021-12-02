"""sisgen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from controluser.views import redirectLogin, returnLogedUser
from controlagenda.views import infoDashboard, searchByDate

urlpatterns = [
    path('admin/', admin.site.urls),
    #path("", TemplateView.as_view(template_name='login.html')),
    path('agendamentos/', include('controlagenda.urls')),
    path('usuarios/', include('controluser.urls')),
    path('', include("django.contrib.auth.urls")),
    path('', redirectLogin, name='login'),
    path('home/', infoDashboard, name='infoDashboard'),
    path('relatorios/', searchByDate, name='searchByDate'),
    path('profile/', returnLogedUser, name='returnLogedUser'),
]

