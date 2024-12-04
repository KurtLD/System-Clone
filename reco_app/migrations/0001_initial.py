# Generated by Django 5.1 on 2024-08-11 08:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('years_of_teaching', models.PositiveIntegerField()),
                ('has_master_degree', models.BooleanField(default=False)),
                ('mobile_web_dev', models.BooleanField(default=False)),
                ('database_management', models.BooleanField(default=False)),
                ('ai_ml', models.BooleanField(default=False)),
                ('iot', models.BooleanField(default=False)),
                ('cybersecurity', models.BooleanField(default=False)),
                ('gis', models.BooleanField(default=False)),
                ('data_analytics', models.BooleanField(default=False)),
                ('ecommerce_digital_marketing', models.BooleanField(default=False)),
                ('educational_technology', models.BooleanField(default=False)),
                ('healthcare_informatics', models.BooleanField(default=False)),
                ('game_development', models.BooleanField(default=False)),
                ('hci', models.BooleanField(default=False)),
                ('agricultural_technology', models.BooleanField(default=False)),
                ('smart_city_technologies', models.BooleanField(default=False)),
                ('fintech', models.BooleanField(default=False)),
                ('computer_networks', models.BooleanField(default=False)),
                ('software_engineering', models.BooleanField(default=False)),
                ('multimedia_graphics', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Adviser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved_title', models.CharField(max_length=255)),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reco_app.faculty')),
            ],
        ),
    ]
