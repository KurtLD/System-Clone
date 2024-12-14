# Generated by Django 5.1 on 2024-12-14 11:44

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_alter_final_evaluationsection_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notif', models.CharField(default='NONE', max_length=255)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('read_by', models.ManyToManyField(blank=True, related_name='read_notifications', to=settings.AUTH_USER_MODEL)),
                ('school_year', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.schoolyear')),
            ],
        ),
        migrations.CreateModel(
            name='UserNotif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read', models.BooleanField(default=False)),
                ('notif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.notif')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'notif')},
            },
        ),
    ]
