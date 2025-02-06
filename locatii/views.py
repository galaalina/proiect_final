from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import *
from .models import *
from .forms import LocatieForm, TurForm, RezervareForm, RecenzieForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
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


#locatii

# afiseaza locatii
def lista_locatie(request):
    locatii = Locatie.objects.all()
    return render(request, 'lista_locatie.html', {'locatii': locatii})


# creeaza locatii
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

# afiseaza detalii locatie
def detalii_locatie(request, locatie_id):
    locatie = get_object_or_404(Locatie, id=locatie_id)
    tururi=locatie.tururi.filter(type='predefinit')

    return render(request, 'detalii_locatie.html', {'locatie': locatie, 'tururi': tururi})

# update/editeaza locatie
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

# sterge locatie
@login_required
@user_passes_test(is_angajat)
def sterge_locatie(request, locatie_id):
    locatie = get_object_or_404(Locatie, id=locatie_id)
    if request.method == "POST":
        locatie.delete()
        return redirect('lista_locatie')

#afiseaza tururile
def lista_tur(request):
    tururi = Tur.objects.filter(type='predefinit')
    return render(request, 'lista_tur.html', {'tururi': tururi})


#creeaza tur
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

# afiseaza detalii tur
def detalii_tur(request, tur_id):
    tur = get_object_or_404(Tur, id=tur_id)
    locatii = tur.locatii.all()
    recenzii = Recenzie.objects.filter(tur=tur).order_by('-pk')[:3]
    user_deja_recenzat = False

    for recenzie in recenzii:
        if recenzie.user == request.user:
            user_deja_recenzat = True

    return render(request, 'detalii_tur.html', {'tur': tur, 'locatii': locatii, 'user_deja_recenzat': user_deja_recenzat })



#update/edit tur
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

#stergere tur
@login_required
@user_passes_test(is_angajat)
def sterge_tur(request, tur_id):
    tur = get_object_or_404(Tur, id=tur_id)
    if request.method == "POST":
        tur.delete()
        return redirect('lista_tur')


# creeaza rezervare
class RezervareCreateView(LoginRequiredMixin, CreateView):
    model = Rezervare
    form_class = RezervareForm
    template_name = 'rezervare_form.html'
    success_url = reverse_lazy('lista_rezervari')

    def form_valid(self, form):
        form.instance.utilizator = self.request.user
        form.instance.suma = form.instance.numar_persoane * form.instance.tur.pret
        return super().form_valid(form)


# afișare rezervările utilizatorului
class RezervarileMeleView(LoginRequiredMixin, ListView):
    model = Rezervare
    template_name = 'rezervarile_mele.html'
    context_object_name = 'rezervari'

    def get_queryset(self):
        return Rezervare.objects.filter(utilizator=self.request.user)

# anulare rezervare
@login_required
def anuleaza_rezervare(request, pk):
    rezervare = get_object_or_404(Rezervare, pk=pk, utilizator=request.user)
    rezervare.delete()
    return redirect('lista_rezervari')


def contact(request):
    return render(request, 'contact.html')

@login_required()
def adauga_recenzie(request, tur_id):
    if request.method == "POST":
        scor = request.POST['scor']
        comentariu = request.POST['comentariu']
        tur = Tur.objects.get(id=tur_id)
        Recenzie.objects.create(
            scor = scor,
            comentariu = comentariu,
            tur = tur,
            user = request.user,
        )
        return redirect('detalii_tur',id=tur_id)

    else:
        return redirect('lista_tur')

class RecezieUpdateView(LoginRequiredMixin, UpdateView):
    template_name='editeaza_recenzie.html'
    form_class = RecenzieForm
    model=Recenzie
    success_url = reverse_lazy('lista_tur')

class RecenzieDeleteView(LoginRequiredMixin, DeleteView):
    template_name='recenzie_confirma_stergerea.html'
    model = Recenzie
    success_url = reverse_lazy('lista_tur')

def afiseaza_recenzii(request, tur_id):
    tur= Tur.objects.get(pk=tur_id)
    recenzii = Recenzie.objects.filter(tur=tur).order_by('-pk')[:3]

    return render(
        request,
        template_name='toate_recenziile.html',
        context ={
            'tur': tur,
            'recenzie': recenzii,
        }
    )






