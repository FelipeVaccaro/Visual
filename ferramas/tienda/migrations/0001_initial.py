# Generated by Django 5.0.6 on 2024-05-18 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('usuario', models.CharField(default='null', max_length=15, primary_key=True, serialize=False, verbose_name='usuario')),
                ('contrasena', models.CharField(default='null', max_length=32, verbose_name='contrasena')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado usuarios')),
            ],
            options={
                'verbose_name': 'usuario',
                'verbose_name_plural': 'usuarios',
            },
        ),
    ]