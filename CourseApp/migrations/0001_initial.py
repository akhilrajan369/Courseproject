# Generated by Django 5.0 on 2024-01-02 14:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50)),
                ('course_fee', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=50)),
                ('student_age', models.IntegerField()),
                ('student_address', models.CharField(max_length=200)),
                ('student_date', models.DateField()),
                ('student_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CourseApp.course')),
            ],
        ),
    ]
