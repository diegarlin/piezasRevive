# Generated by Django 4.2.7 on 2023-11-27 11:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reclamaciones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reclamacion',
            name='descripcion',
            field=models.TextField(default=' '),
        ),
        migrations.AlterField(
            model_name='reclamacion',
            name='motivo',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='reclamacion',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
