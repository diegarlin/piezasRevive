# Generated by Django 4.2.7 on 2023-11-25 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0002_pedido_gastos_envio'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='precio_final',
            field=models.IntegerField(default=0),
        ),
    ]
