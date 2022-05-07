# Generated by Django 4.0.4 on 2022-05-07 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_course_course_name_course_creation_time_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='course_headman',
            new_name='headman',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='course_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='group',
            old_name='group_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='subject',
            old_name='subject_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='subject',
            old_name='teachers',
            new_name='teacher',
        ),
        migrations.AlterField(
            model_name='person',
            name='person_type',
            field=models.CharField(choices=[('STD', 'Student'), ('TCH', 'Teacher')], default='STD', max_length=3),
        ),
    ]