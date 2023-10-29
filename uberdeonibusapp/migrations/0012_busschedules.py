# Generated by Django 4.2.5 on 2023-10-29 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uberdeonibusapp', '0011_alter_location_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusSchedules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule', models.DateTimeField()),
                ('route', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='uberdeonibusapp.busroute')),
            ],
            options={
                'verbose_name': 'Horário',
                'verbose_name_plural': 'Horários',
            },
        ),
    ]
