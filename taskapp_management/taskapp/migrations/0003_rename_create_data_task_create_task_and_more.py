# Generated by Django 4.2 on 2024-09-21 12:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taskapp', '0002_alter_task_create_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='create_data',
            new_name='create_task',
        ),
        migrations.AlterField(
            model_name='task',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
