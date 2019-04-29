# Generated by Django 2.0.6 on 2019-04-29 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='descripcion',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='direccion',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='ruc',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]
