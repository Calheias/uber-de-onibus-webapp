# Generated by Django 4.2.5 on 2023-10-19 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uberdeonibusapp', '0002_busroute_location_remove_grade_course_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='latitude',
            field=models.DecimalField(decimal_places=7, max_digits=9),
        ),
        migrations.AlterField(
            model_name='location',
            name='longitude',
            field=models.DecimalField(decimal_places=7, max_digits=9),
        ),
    ]