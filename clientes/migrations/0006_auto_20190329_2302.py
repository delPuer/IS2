# Generated by Django 2.0.6 on 2019-03-29 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0005_auto_20190329_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='descripcion_cliente',
            field=models.TextField(max_length=300),
        ),
    ]
