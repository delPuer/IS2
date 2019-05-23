# Generated by Django 2.0.6 on 2019-05-13 02:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sprint', '0014_auto_20190512_2048'),
    ]

    operations = [
        migrations.CreateModel(
            name='Horas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horas_laborales', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='dialaboral',
            name='sprint',
        ),
        migrations.RemoveField(
            model_name='dialaboral',
            name='team_member',
        ),
        migrations.RemoveField(
            model_name='sprint',
            name='fecha_fin_estimada',
        ),
        migrations.RemoveField(
            model_name='sprint',
            name='fecha_ini_estimada',
        ),
        migrations.AddField(
            model_name='sprint',
            name='dias_laborales',
            field=models.IntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='DiaLaboral',
        ),
        migrations.AddField(
            model_name='horas',
            name='sprint',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sprint.Sprint'),
        ),
        migrations.AddField(
            model_name='horas',
            name='team_member',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
