# Generated by Django 4.2 on 2025-01-16 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locatii', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locatie',
            name='descriere',
            field=models.TextField(blank=True, null=True),
        ),
    ]
