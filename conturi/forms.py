from django.db.transaction import atomic
from django.forms import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.transaction import atomic
from django.forms import CharField, TextInput
from .models import Profile

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
        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
        }

    @atomic
    def save(self, commit=True):

        user = super().save(commit)

        data_telefon = self.cleaned_data['telefon']
        # Creăm un obiect Profile în care adăugăm datele noastre extra
        profile = Profile(user=user, telefon=data_telefon)
        if commit:
            profile.save()

        return user




class ProfileForm(ModelForm):
    telefon = CharField(required=True, widget=TextInput(attrs={'class': 'form-control'}))


    class Meta:
        model = Profile
        fields = ['telefon']
