from django.forms import *

from locatii.models import Locatie, Tur


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
            'pret': TextInput(attrs={'class': 'form-control', 'placeholder': 'Prețul turului'}),
            'pachet': Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Detalii pachet...'}),
            'imagine_tur': ClearableFileInput(attrs={'class': 'form-control'}),
        }
