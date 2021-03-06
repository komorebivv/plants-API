# Generated by Django 3.2.6 on 2021-08-30 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='required_exposure',
            field=models.IntegerField(choices=[('dark', 'dark'), ('shade', 'shade'), ('partysun', 'part sun'), ('fullsun', 'full sun')], verbose_name='Exposure'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='required_humidity',
            field=models.IntegerField(choices=[(1, 'low'), (2, 'medium'), (3, 'high')], verbose_name='Humidity'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='required_temperature',
            field=models.IntegerField(choices=[(1, 'cold'), (2, 'medium'), (3, 'warm')], verbose_name='Temperature'),
        ),
    ]
