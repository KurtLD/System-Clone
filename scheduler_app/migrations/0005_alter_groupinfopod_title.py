# Generated by Django 5.1 on 2024-08-25 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler_app', '0004_groupinfopod_title_schedule_created_at_schedule_day_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupinfopod',
            name='title',
            field=models.CharField(default='None', max_length=200, null=True),
        ),
    ]
