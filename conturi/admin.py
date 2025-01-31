from django.contrib import admin

# Register your models here.

from conturi.models import Profile
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class CustomUserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ('user_groups',)  # Show groups in the user list

    def user_groups(self, obj):
        return ", ".join([group.name for group in obj.groups.all()]) if obj.groups.exists() else "No Group"

    user_groups.short_description = "Groups"


admin.site.unregister(User)  # Unregister the default UserAdmin
admin.site.register(User, CustomUserAdmin)  # Register the custom one

admin.site.register(Profile)