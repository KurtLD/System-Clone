# Generated by Django 5.1 on 2024-10-03 02:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler_app', '0005_alter_groupinfopod_title'),
        ('users', '0018_mock_evaluationsection_schoolyear_mock_criteria_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupinfopod',
            name='school_year',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.schoolyear'),
        ),
        migrations.AddField(
            model_name='groupinfoth',
            name='school_year',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.schoolyear'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='school_year',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.schoolyear'),
        ),
        migrations.AddField(
            model_name='schedulepod',
            name='school_year',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.schoolyear'),
        ),
    ]
