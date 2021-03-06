# Generated by Django 2.2 on 2019-04-06 13:41

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import rest_framework.compat


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(db_index=True, max_length=256)),
                ('max_score', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0),
                                                                           django.core.validators.MaxValueValidator(
                                                                               100)])),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='examsheets',
                                              to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('creator', 'title')},
            },
        ),
        migrations.CreateModel(
            name='TaskSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('question', models.CharField(db_index=True, max_length=512)),
                ('score',
                 models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('answer', models.TextField()),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_sheets',
                                              to=settings.AUTH_USER_MODEL)),
                ('exam_sheet',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_sheets',
                                   to='exams_api.ExamSheet')),
            ],
            options={
                'unique_together': {('creator', 'question', 'exam_sheet')},
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('answer', models.TextField()),
                ('score',
                 models.PositiveSmallIntegerField(default=0, validators=[rest_framework.compat.MinValueValidator(0)])),
                ('task_sheet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks',
                                                 to='exams_api.TaskSheet')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks',
                                           to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'task_sheet')},
            },
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('exam_sheet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exams',
                                                 to='exams_api.ExamSheet')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exams',
                                           to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'exam_sheet')},
            },
        ),
    ]
