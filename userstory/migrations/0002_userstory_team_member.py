# Generated by Django 2.0.6 on 2019-04-27 00:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userstory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstory',
            name='team_member',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]