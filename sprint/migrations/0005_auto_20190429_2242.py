# Generated by Django 2.0.6 on 2019-04-29 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sprint', '0004_auto_20190429_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sprint',
            name='duracion',
            field=models.DurationField(blank=True, null=True),
        ),
    ]