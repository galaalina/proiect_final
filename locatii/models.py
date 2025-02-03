from django.contrib.auth.models import User
from django.db import models
from django.db.models import *
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Judet(models.Model):
    class Meta:
        verbose_name_plural = 'Judete'
    nume = CharField(max_length=128)
    descriere = TextField()

    def __str__(self):
        return self.nume

class Oras(models.Model):
    class Meta:
        verbose_name_plural = 'Orase'
    nume = CharField(max_length=128)
    descriere = TextField()
    judet = ForeignKey(Judet, on_delete=CASCADE, related_name='orase')

    def __str__(self):
        return f"{self.nume}"

class Locatie(models.Model):
    class Meta:
        verbose_name_plural = 'Locatii'
    nume = CharField(max_length=128)
    descriere = TextField(blank=True, null=True)
    oras = ForeignKey(Oras, on_delete=CASCADE, related_name='locatii')
    judet = ForeignKey(Judet, on_delete=CASCADE, related_name='locatii')
    imagine_locatie = ImageField(upload_to='imagini', blank=True, null=True)
    def __str__(self):
        return f"{self.nume}"


class Tur(models.Model):
    class Meta:
        verbose_name_plural = 'Tururi'
    OPTIUNI_TIP_TUR = [
            ('predefinit', 'Predefinit'),
            ('personalizat', 'Personalizat')
        ]
    nume = CharField(max_length=128, blank=True, null=True)
    descriere = TextField(blank=True, null=True)
    locatii = ManyToManyField(Locatie, related_name='tururi')
    type = CharField(max_length=40, choices=OPTIUNI_TIP_TUR, default='predefinit' )
    durata= CharField(max_length=128, blank=True, null=True)
    pret = CharField(max_length=256, blank=True, null=True)
    pachet = TextField(blank=True, null=True)
    imagine_tur = ImageField(upload_to='imagini', blank=True, null=True)

    def __str__(self):
        return f"{self.nume}"

class Rezervare(models.Model):
    class Meta:
        verbose_name_plural = 'Rezervari'

    OPTIUNI_STATUS = [
        ('in asteptare', 'In asteptare'),
        ('in procesare', 'In procesare'),
        ('confirmata', 'Confirmata')
    ]
    utilizator = ForeignKey(User, on_delete=CASCADE, related_name='rezervari')
    numar_persoane= PositiveIntegerField(blank=False, null=False, default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])
    tur = ForeignKey(Tur, on_delete=CASCADE, related_name='rezervari')
    data_inceput = DateField()
    creata = DateField(auto_now_add=True)
    status = CharField(max_length=40, choices=OPTIUNI_STATUS, default='in asteptare' )

    def __str__(self):
        return f"{self.tur}, {self.utilizator}"
