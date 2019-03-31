# Generated by Django 2.0.6 on 2019-03-31 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=300)),
                ('direccion', models.CharField(max_length=200)),
                ('ruc', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=30)),
            ],
        ),
    ]
