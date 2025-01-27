from django.shortcuts import *
from .models import Locatie, Tur, Judet, Oras

# Create your views here.
def lista_locatie(request):
    locatii = Locatie.objects.all()
    return render(request, 'lista_locatie.html', {'locatii': locatii})

def detalii_locatie(request, locatie_id):
    locatie = get_object_or_404(Locatie, id=locatie_id)
    tururi=locatie.tururi.filter(type='predefinit')

    return render(request, 'detalii_locatie.html', {'locatie': locatie, 'tururi': tururi})

def lista_tur(request):
    tururi = Tur.objects.filter(type='predefinit')
    return render(request, 'lista_tur.html', {'tururi': tururi})

def detalii_tur(request, tur_id):
    tur = get_object_or_404(Tur, id=tur_id)
    locatii = tur.locatii.all()
    return render(request, 'detalii_tur.html', {'tur': tur, 'locatii': locatii})

def creare_tur_personalizat(request):
    locatii = Locatie.objects.all()
    if request.method == 'POST':
        ids_locatie_selectata = request.POST.getlist('locatii')
        locatii_selectate = Locatie.objects.filter(id__in=ids_locatie_selectata)
        tur_personalizat = Tur.objects.create(
            nume='Tur Personalizat',
            descriere="Un tur definit de client",
            type='personalizat'
        )
        tur_personalizat.locatii.set(locatii_selectate)
        return render(request, 'succes_tur_personalizat.html', {'tur': tur_personalizat})
    return render(request, 'creare_tur_personalizat.html', {'locatii': locatii})





