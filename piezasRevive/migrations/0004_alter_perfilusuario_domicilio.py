# Generated by Django 4.2.7 on 2023-11-27 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piezasRevive', '0003_perfilusuario_domicilio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfilusuario',
            name='domicilio',
            field=models.CharField(default='Avenida Reina Mercedes S/N ETSII', max_length=300),
        ),
    ]
