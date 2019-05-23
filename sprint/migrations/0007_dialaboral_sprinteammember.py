# Generated by Django 2.0.6 on 2019-05-12 00:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sprint', '0006_auto_20190501_1852'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiaLaboral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.CharField(choices=[(1, 'Lunes'), (2, 'Martes'), (3, 'Miercoles'), (4, 'Jueves'), (5, 'Viernes'), (6, 'Sabado'), (7, 'Domingo')], max_length=20)),
                ('horas_laborales', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SprinTeamMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sprint', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sprint.Sprint')),
                ('dias_laborales', models.ManyToManyField(to='sprint.DiaLaboral')),
                ('usuario', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
