# Generated by Django 5.2 on 2025-05-01 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='clase',
            field=models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='Clase'),
        ),
    ]
