# Generated by Django 5.1 on 2024-11-12 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler_app', '0016_schedulepod_new_sched'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='new_sched',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='schedulefd',
            name='new_sched',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='schedulemd',
            name='new_sched',
            field=models.BooleanField(default=False),
        ),
    ]
