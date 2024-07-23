# Generated by Django 5.0.1 on 2024-07-20 09:57

import admins.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0010_quiz_due_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='is_available_to_students',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='due_date',
            field=models.DateTimeField(default=admins.models.one_day_from_now),
        ),
    ]