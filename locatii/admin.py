from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import Judet, Oras, Locatie, Tur, Rezervare

# Register your models here.
admin.site.register(Judet)
admin.site.register(Oras)



@admin.register(Rezervare)
class RezervareAdmin(admin.ModelAdmin):
    list_display = ('utilizator', 'tur', 'numar_persoane', 'creata', 'data_inceput', 'status','edit_button', 'delete_button')
    list_filter = ('utilizator', 'tur','data_inceput', 'status')
    ordering = ('data_inceput','status')

    def edit_button(self, obj):
        url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name), args=[obj.pk])
        return format_html('<a href="{}" style="color:blue;">✏️</a>', url)

    def delete_button(self, obj):
        url = reverse('admin:%s_%s_delete' % (obj._meta.app_label, obj._meta.model_name), args=[obj.pk])
        return format_html('<a href="{}" style="color:red;">❌</a>', url)

@admin.register(Tur)
class TurAdmin(admin.ModelAdmin):
    list_display = ('nume', 'type', 'pachet', 'edit_button', 'delete_button')
    list_filter = ('nume', 'type')

    def edit_button(self, obj):
        url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name), args=[obj.pk])
        return format_html('<a href="{}" style="color:blue;">✏️</a>', url)

    def delete_button(self, obj):
        url = reverse('admin:%s_%s_delete' % (obj._meta.app_label, obj._meta.model_name), args=[obj.pk])
        return format_html('<a href="{}" style="color:red;">❌</a>', url)

@admin.register(Locatie)
class LocatieAdmin(admin.ModelAdmin):
    list_display = ('nume', 'oras', 'judet', 'edit_button', 'delete_button')
    list_filter = ('oras', 'judet' )


    def edit_button(self, obj):
        url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name), args=[obj.pk])
        return format_html('<a href="{}" style="color:blue;">✏️</a>', url)

    def delete_button(self, obj):
        url = reverse('admin:%s_%s_delete' % (obj._meta.app_label, obj._meta.model_name), args=[obj.pk])
        return format_html('<a href="{}" style="color:red;">❌</a>', url)



