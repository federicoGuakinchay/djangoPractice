# Generated by Django 4.2 on 2024-09-23 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0011_importance_task_importance_value_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='limit_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
