
from django.db import models
from django.db.models import *
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    class Meta:
        verbose_name_plural = 'Profiluri'
    user = OneToOneField(User, on_delete=models.CASCADE)
    telefon = CharField(max_length=20, blank=False, null=False)


    def __str__(self):
        return self.user.username