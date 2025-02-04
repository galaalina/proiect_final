# Generated by Django 4.2 on 2025-02-04 11:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('locatii', '0013_rezervare_suma_alter_tur_pret'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recenzie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=5)),
                ('comentariu', models.TextField(blank=True, null=True)),
                ('data_crearii', models.DateTimeField(auto_now_add=True)),
                ('tur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recenzii', to='locatii.tur')),
                ('utilizator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
