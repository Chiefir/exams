# Generated by Django 2.2 on 2019-04-03 19:29

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exams_api', '0002_auto_20190403_2117'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='tasksheet',
            unique_together={('creator', 'question', 'exam_sheet')},
        ),
        migrations.RemoveField(
            model_name='tasksheet',
            name='title',
        ),
    ]
