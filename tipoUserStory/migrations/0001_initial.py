# Generated by Django 2.0.6 on 2019-04-27 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('proyecto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoUserStory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.TextField()),
                ('flujos', models.ManyToManyField(to='proyecto.Flujo')),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.Proyecto')),
            ],
        ),
    ]
