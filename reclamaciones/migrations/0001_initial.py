# Generated by Django 4.2.7 on 2023-11-21 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pedido', '0001_initial'),
        ('piezasRevive', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reclamacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo', models.TextField()),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedido.pedido')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='piezasRevive.perfilusuario')),
            ],
        ),
    ]