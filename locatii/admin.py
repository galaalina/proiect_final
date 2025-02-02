from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import Judet, Oras, Locatie, Tur, Ghid, Transport, Rezervare

# Register your models here.
admin.site.register(Judet)
admin.site.register(Oras)
admin.site.register(Locatie)
admin.site.register(Tur)
admin.site.register(Ghid)
admin.site.register(Transport)


@admin.register(Rezervare)
class RezervareAdmin(admin.ModelAdmin):
    list_display = ('utilizator', 'tur', 'numar_persoane', 'creata', 'data_inceput', 'edit_button', 'delete_button')
    list_filter = ('utilizator', 'tur','data_inceput')
    ordering = ('data_inceput',)

    def edit_button(self, obj):
        url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name), args=[obj.pk])
        return format_html('<a class="button" href="{}" style="color:blue;">✏️ Editare</a>', url)

    def delete_button(self, obj):
        url = reverse('admin:%s_%s_delete' % (obj._meta.app_label, obj._meta.model_name), args=[obj.pk])
        return format_html('<a class="button" href="{}" style="color:red;">❌ Ștergere</a>', url)


    edit_button.short_description = "Editare"
    delete_button.short_description = "Ștergere"