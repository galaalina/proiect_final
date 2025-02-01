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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from conturi import urls as conturi_urls

from locatii import views
from locatii.views import RezervareCreateView, RezervarileMeleView, anuleaza_rezervare, editeaza_tur, sterge_tur, \
    sterge_locatie, editeaza_locatie, contact

# from locatii.views import lista_locatie, detalii_locatie, lista_tur, detalii_tur


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.acasa, name='acasa'),
    path('contact/', contact, name='contact'),


    #Locatii
    path('locatii/', views.lista_locatie, name='lista_locatie'),
    path('locatii/<int:locatie_id>/', views.detalii_locatie, name='detalii_locatie'),
    path('adauga_locatie/', views.adauga_locatie, name='adauga_locatie'),
    path('locatie/<int:locatie_id>/edit/', editeaza_locatie, name='editeaza_locatie'),
    path('locatie/<int:locatie_id>/delete/', sterge_locatie, name='sterge_locatie'),
    #Tururi
    path('tururi/', views.lista_tur, name='lista_tur'),
    path('tururi/<int:tur_id>/', views.detalii_tur, name='detalii_tur'),
    path('adauga_tur/', views.adauga_tur, name='adauga_tur'),
    path('tur/<int:tur_id>/edit/', editeaza_tur, name='editeaza_tur'),
    path('tur/<int:tur_id>/delete/', sterge_tur, name='sterge_tur'),
    # conturi
    path("conturi/", include(conturi_urls, namespace='conturi')),
    # rezervari
    path('rezervare/', RezervareCreateView.as_view(), name='creeaza_rezervare'),
    path('rezervarile-mele/', RezervarileMeleView.as_view(), name='lista_rezervari'),
    path('rezervare/anuleaza/<int:pk>/', anuleaza_rezervare, name='anuleaza_rezervare'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)