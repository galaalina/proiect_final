from django.db import models
from django.db.models import *

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
        return f"{self.nume}, {self.judet.nume}"

class Locatie(models.Model):
    class Meta:
        verbose_name_plural = 'Locatii'
    nume = CharField(max_length=128)
    descriere = TextField(blank=True, null=True)
    oras = ForeignKey(Oras, on_delete=CASCADE, related_name='locatii')
    judet = ForeignKey(Judet, on_delete=CASCADE, related_name='locatii')
    def __str__(self):
        return f"{self.nume}, {self.oras.nume},{self.judet.nume}"


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

    def __str__(self):
        return f"{self.nume}"

