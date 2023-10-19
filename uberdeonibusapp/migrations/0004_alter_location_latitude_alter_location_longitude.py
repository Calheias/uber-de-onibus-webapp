# Generated by Django 4.2.5 on 2023-10-19 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uberdeonibusapp', '0003_alter_location_latitude_alter_location_longitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='latitude',
            field=models.DecimalField(decimal_places=15, max_digits=20),
        ),
        migrations.AlterField(
            model_name='location',
            name='longitude',
            field=models.DecimalField(decimal_places=15, max_digits=20),
        ),
    ]
