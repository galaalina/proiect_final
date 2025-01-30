from django.forms import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile

class UserRegisterForm(UserCreationForm):
    nume = CharField(required=True, widget=TextInput(attrs={'class': 'form-control'}))
    prenume = CharField(required=True, widget=TextInput(attrs={'class': 'form-control'}))
    email = EmailField(required=True, widget=EmailInput(attrs={'class': 'form-control'}))
    telefon = CharField(required=True, widget=TextInput(attrs={'class': 'form-control'}))


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.last_name = self.cleaned_data['nume']
        user.first_name = self.cleaned_data['prenume']
        user.telephone = self.cleaned_data['telefon']
        if commit:
            user.save()
        return user

class ProfileForm(ModelForm):
    telefon = CharField(required=True, widget=TextInput(attrs={'class': 'form-control'}))


    class Meta:
        model = Profile
        fields = ['telefon']
