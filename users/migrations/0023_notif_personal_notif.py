# Generated by Django 5.1 on 2024-12-17 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_notif_usernotif'),
    ]

    operations = [
        migrations.AddField(
            model_name='notif',
            name='personal_notif',
            field=models.BooleanField(default=False),
        ),
    ]
