# Generated by Django 2.0.6 on 2019-04-29 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tipoUserStory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipouserstory',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
    ]
