# Generated by Django 5.1 on 2024-10-11 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_alter_preoral_evaluationsection_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='final_evaluationsection',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='mock_evaluationsection',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
