# Generated by Django 2.0.6 on 2019-05-19 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sprint', '0017_auto_20190515_1635'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sprint',
            name='duracion',
        ),
        migrations.AlterField(
            model_name='horas',
            name='horas_laborales',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='sprint',
            name='dias_laborales',
            field=models.IntegerField(),
        ),
    ]
