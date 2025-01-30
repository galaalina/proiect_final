from django.db.transaction import atomic
from django.forms import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile

from django.contrib.auth.forms import UserCreationForm
from django.db.transaction import atomic
from django.forms import CharField, TextInput
from .models import Profile  # Asigură-te că importi modelul Profile

class UserRegisterForm(UserCreationForm):
    telefon = CharField(required=True, widget=TextInput(attrs={'class': 'form-control'}))

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'last_name', 'first_name', 'email']
        labels = {
            'username': 'Nume utilizator',
            'first_name': 'Prenume',
            'last_name': 'Nume',
            'email': 'Adresă email',
        }

    @atomic
    def save(self, commit=True):
        # Salvăm obiectul User care provine din Django
        user = super().save(commit)

        data_telefon = self.cleaned_data['telefon']
        # Creăm un obiect Profile în care adăugăm datele noastre extra
        profile = Profile(user=user, telefon=data_telefon)
        if commit:
            profile.save()

        return user


    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.last_name = self.cleaned_data['nume']
    #     user.first_name = self.cleaned_data['prenume']
    #     if commit:
    #         user.save()
    #     return user

class ProfileForm(ModelForm):
    telefon = CharField(required=True, widget=TextInput(attrs={'class': 'form-control'}))


    class Meta:
        model = Profile
        fields = ['telefon']
