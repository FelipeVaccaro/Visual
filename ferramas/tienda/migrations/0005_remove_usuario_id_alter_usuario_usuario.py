# Generated by Django 5.0.6 on 2024-05-23 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0004_usuario_id_alter_usuario_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='id',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='usuario',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='usuario'),
        ),
    ]
