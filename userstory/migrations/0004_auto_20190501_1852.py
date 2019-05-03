# Generated by Django 2.0.6 on 2019-05-01 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userstory', '0003_auto_20190501_1455'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userstory',
            name='estado_flujo',
        ),
        migrations.AddField(
            model_name='userstory',
            name='estado_fase',
            field=models.CharField(choices=[('To Do', 'To Do'), ('Doing', 'Doing'), ('Done', 'Done')], default='To Do', max_length=30),
        ),
    ]
