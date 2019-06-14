# Generated by Django 2.0.6 on 2019-05-26 20:28

from django.db import migrations, models
import django.db.models.deletion
import userstory.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sprint', '0001_initial'),
        ('proyecto', '0001_initial'),
        ('flujo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.TextField()),
                ('duracion', models.IntegerField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Archivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=255)),
                ('archivo', models.FileField(upload_to='')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserStory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_fase', models.CharField(choices=[('To Do', 'To Do'), ('Doing', 'Doing'), ('Done', 'Done'), ('Control de Calidad', 'Control de Calidad')], default='To Do', max_length=30)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=300)),
                ('fecha_inicio', models.DateField(blank=True, null=True, verbose_name='Fecha de inicio del User Story')),
                ('duracion_estimada', models.IntegerField()),
                ('valor_negocio', models.PositiveIntegerField(validators=[userstory.models.rango])),
                ('prioridad', models.PositiveIntegerField(validators=[userstory.models.rango])),
                ('valor_tecnico', models.PositiveIntegerField(validators=[userstory.models.rango])),
                ('estado', models.PositiveIntegerField(choices=[(2, 'Pendiente'), (1, 'Asignado'), (0, 'Finalizado')], default=2)),
                ('fase', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='flujo.Fase')),
                ('flujo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='flujo.Flujo')),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.Proyecto')),
                ('sprint', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='sprint.Sprint')),
                ('sprints_asignados', models.ManyToManyField(blank=True, related_name='userstory_sprint_asignado', to='sprint.Sprint')),
            ],
        ),
    ]
