# Generated by Django 2.0.6 on 2019-05-04 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userstory', '0008_actividad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstory',
            name='estado_fase',
            field=models.CharField(choices=[('To Do', 'To Do'), ('Doing', 'Doing'), ('Done', 'Done'), ('Control de Calidad', 'Control de Calidad')], default='To Do', max_length=30),
        ),
    ]
