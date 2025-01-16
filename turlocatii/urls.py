"""
URL configuration for turlocatii project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from locatii import views
# from locatii.views import lista_locatie

urlpatterns = [
    path('admin/', admin.site.urls),
    #Locatii
    path('locatii/', views.lista_locatie, name='lista_locatie'),
    path('locatii/<int:locatie_id>/', views.detalii_locatie, name='detalii_locatie'),
    #Tururi
    path('tururi/', views.lista_tur, name='lista_tur'),
    path('tururi/<int:tur_id>/', views.detalii_tur, name='detalii_tur'),

    #Creare tur personalizat
    path('tur_personalizat/creare', views.creare_tur_personalizat, name='creare_tur_personalizat'),
]
