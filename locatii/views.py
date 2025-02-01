from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import *
from .models import *
from .forms import LocatieForm, TurForm, RezervareForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, ListView, UpdateView
from django.urls import reverse_lazy

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

def is_angajat(user):
    return user.is_authenticated and user.groups.filter(name='angajati').exists()

@login_required
@user_passes_test(is_angajat)
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



@login_required
@user_passes_test(is_angajat)
def editeaza_locatie(request, locatie_id):
    locatie = get_object_or_404(Locatie, id=locatie_id)
    if request.method == "POST":
        form = LocatieForm(request.POST, request.FILES, instance=locatie)
        if form.is_valid():
            form.save()
            return redirect('detalii_locatie', locatie_id=locatie.id)
    else:
        form = LocatieForm(instance=locatie)

    return render(request, 'adauga_locatie.html', {'form': form, 'locatie':locatie})

@login_required
@user_passes_test(is_angajat)
def sterge_locatie(request, locatie_id):
    locatie = get_object_or_404(Locatie, id=locatie_id)
    if request.method == "POST":
        locatie.delete()
        return redirect('lista_locatie')

    return render(request, 'confirmare_stergere.html', {'tlocatie': locatie})



def lista_tur(request):
    tururi = Tur.objects.filter(type='predefinit')
    return render(request, 'lista_tur.html', {'tururi': tururi})



@login_required
@user_passes_test(is_angajat)
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

@login_required
@user_passes_test(is_angajat)
def editeaza_tur(request, tur_id):
    tur = get_object_or_404(Tur, id=tur_id)
    if request.method == "POST":
        form = TurForm(request.POST, request.FILES, instance=tur)
        if form.is_valid():
            form.save()
            return redirect('detalii_tur', tur_id=tur.id)
    else:
        form = TurForm(instance=tur)

    return render(request, 'adauga_tur.html', {'form': form, 'tur': tur})

@login_required
@user_passes_test(is_angajat)
def sterge_tur(request, tur_id):
    tur = get_object_or_404(Tur, id=tur_id)
    if request.method == "POST":
        tur.delete()
        return redirect('lista_tur')

    return render(request, 'confirmare_stergere.html', {'tur': tur})


# Creare rezervare
class RezervareCreateView(LoginRequiredMixin, CreateView):
    model = Rezervare
    form_class = RezervareForm
    template_name = 'rezervare_form.html'
    success_url = reverse_lazy('lista_rezervari')

    def form_valid(self, form):
        form.instance.utilizator = self.request.user
        return super().form_valid(form)

# Afișare rezervările utilizatorului
class RezervarileMeleView(LoginRequiredMixin, ListView):
    model = Rezervare
    template_name = 'rezervarile_mele.html'
    context_object_name = 'rezervari'

    def get_queryset(self):
        return Rezervare.objects.filter(utilizator=self.request.user)

# Anularea unei rezervări
@login_required
def anuleaza_rezervare(request, pk):
    rezervare = get_object_or_404(Rezervare, pk=pk, utilizator=request.user)
    rezervare.delete()
    return redirect('lista_rezervari')








