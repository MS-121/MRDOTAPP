# Generated by Django 2.2.6 on 2019-10-20 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UMI', '0005_auto_20191020_1043'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prescribtion',
            options={'ordering': ('prescribtion_content',)},
        ),
        migrations.AlterField(
            model_name='duration',
            name='duration',
            field=models.TimeField(),
        ),
    ]
