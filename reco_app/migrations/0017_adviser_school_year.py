# Generated by Django 5.1 on 2024-10-03 18:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reco_app', '0016_adviser_group_name_alter_faculty_expertise_and_more'),
        ('users', '0018_mock_evaluationsection_schoolyear_mock_criteria_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='adviser',
            name='school_year',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.schoolyear'),
        ),
    ]
