# Generated by Django 4.2 on 2024-09-21 12:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='create_data',
            field=models.DateField(default=django.utils.timezone.now, null=True),
        ),
    ]
