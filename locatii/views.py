from django.shortcuts import *
from .models import Locatie, Tur, Judet, Oras
from .forms import LocatieForm, TurForm

# Create your views here.

# views.py

def acasa(request):
    # Limitează la 3 locații
    locatii = Locatie.objects.all()[:3]  # Selectează primele 3 locații

    # Limitează la 3 tururi
    tururi = Tur.objects.all()[:3]  # Selectează primele 3 tururi

    return render(request, 'acasa.html', {
        'locatii': locatii,
        'tururi': tururi,
    })

def lista_locatie(request):
    locatii = Locatie.objects.all()
    return render(request, 'lista_locatie.html', {'locatii': locatii})

def adauga_locatie(request):
    if request.method == "POST":
        form = LocatieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_locatie')  # Redirecționează către lista locațiilor
        else:
            # Renderizează pagina de adăugare a locației cu erorile formularului
            return render(request, 'adauga_locatie.html', {'form': form})
    else:
        # Formular gol pentru metoda GET
        form = LocatieForm()
        return render(request, 'adauga_locatie.html', {'form': form})


def detalii_locatie(request, locatie_id):
    locatie = get_object_or_404(Locatie, id=locatie_id)
    tururi=locatie.tururi.filter(type='predefinit')

    return render(request, 'detalii_locatie.html', {'locatie': locatie, 'tururi': tururi})

def lista_tur(request):
    tururi = Tur.objects.filter(type='predefinit')
    return render(request, 'lista_tur.html', {'tururi': tururi})





def adauga_tur(request):
    if request.method == 'POST':
        form = TurForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_tur') # Redirecționează după salvarea turului
        else:
            return render(request, 'adauga_tur.html', {'form': form})
    else:
        form = TurForm()
        return render(request, 'adauga_tur.html', {'form': form})


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





