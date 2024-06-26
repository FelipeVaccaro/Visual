# Generated by Django 5.0.6 on 2024-05-31 04:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0011_alter_producto_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.IntegerField(default=1)),
                ('cantidad', models.IntegerField(default=1)),
                ('direccion', models.CharField(blank=True, default='', max_length=100)),
                ('telefono', models.CharField(blank=True, default='', max_length=20)),
                ('fecha', models.DateField(default=datetime.datetime.today)),
                ('estado', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
    ]
