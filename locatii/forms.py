from django.forms import *

from locatii.models import Locatie, Tur, Rezervare, Recenzie


class LocatieForm(ModelForm):
    class Meta:
        model = Locatie
        fields = ['nume', 'descriere', 'oras', 'judet', 'imagine_locatie']
        widgets = {
            'nume': TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduceți numele locației'}),
            'descriere': Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Descriere...'}),
            'oras': Select(attrs={'class': 'form-control'}),
            'judet': Select(attrs={'class': 'form-control'}),
            'imagine_locatie': ClearableFileInput(attrs={'class': 'form-control'}),
        }



class TurForm(ModelForm):
    class Meta:
        model = Tur
        fields = ['nume', 'descriere', 'locatii', 'type', 'durata', 'pret', 'pachet', 'imagine_tur']
        widgets = {
            'nume': TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduceți numele turului'}),
            'descriere': Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Descriere...'}),
            'locatii': SelectMultiple(attrs={'class': 'form-control'}),
            'type': Select(attrs={'class': 'form-control'}),
            'durata': TextInput(attrs={'class': 'form-control', 'placeholder': 'Durata turului'}),
            'pret': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Prețul turului'}),
            'pachet': Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Detalii pachet...'}),
            'imagine_tur': ClearableFileInput(attrs={'class': 'form-control'}),
        }



class RezervareForm(ModelForm):
    class Meta:
        model = Rezervare
        fields = ['numar_persoane', 'tur', 'data_inceput']
        widgets = {
            'numar_persoane':NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 10}),
            'tur': Select(attrs={'class': 'form-control'}),
            'data_inceput': DateInput(attrs={'type': 'date', 'class': 'form-control'})

        }

class RecenzieForm(ModelForm):
    class Meta:
        model = Recenzie
        fields = ['scor', 'comentariu']



from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(
        label="Caută locație",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Caută locație...'})
    )

