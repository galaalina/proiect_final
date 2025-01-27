from django.contrib import admin

from .models import Judet, Oras, Locatie, Tur, Ghid, Transport

# Register your models here.
admin.site.register(Judet)
admin.site.register(Oras)
admin.site.register(Locatie)
admin.site.register(Tur)
admin.site.register(Ghid)
admin.site.register(Transport)