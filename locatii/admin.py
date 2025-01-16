from django.contrib import admin

from .models import Judet, Oras, Locatie, Tur

# Register your models here.
admin.site.register(Judet)
admin.site.register(Oras)
admin.site.register(Locatie)
admin.site.register(Tur)