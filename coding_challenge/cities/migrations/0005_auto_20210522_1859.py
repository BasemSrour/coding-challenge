# Generated by Django 3.1.11 on 2021-05-22 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0004_auto_20210522_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='latitude',
            field=models.FloatField(verbose_name='Latitude'),
        ),
        migrations.AlterField(
            model_name='city',
            name='longitude',
            field=models.FloatField(verbose_name='Longitude'),
        ),
    ]
