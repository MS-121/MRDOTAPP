# Generated by Django 2.2.6 on 2019-10-20 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UMI', '0004_remove_appointment_disease_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='doctor_id',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='patient_id',
        ),
    ]