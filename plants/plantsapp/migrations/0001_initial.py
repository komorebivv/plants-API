# Generated by Django 3.2.6 on 2021-08-26 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=80, unique=True, verbose_name='Name of category')),
                ('slug', models.SlugField(max_length=80, unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True, verbose_name='Name of Room')),
                ('temperature', models.IntegerField(choices=[(1, 'cold'), (2, 'medium'), (3, 'warm')], verbose_name='Temperature')),
                ('expose', models.CharField(choices=[('dark', 'dark'), ('shade', 'shade'), ('partysun', 'part sun'), ('fullsun', 'full sun')], max_length=10, verbose_name='Exposure')),
                ('humidity', models.CharField(choices=[(1, 'low'), (2, 'medium'), (3, 'high')], max_length=10, verbose_name='Humidity')),
                ('draft', models.BooleanField(blank=True, default=False, verbose_name='Draft')),
            ],
            options={
                'verbose_name': 'Room',
                'verbose_name_plural': 'Rooms',
            },
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='Name')),
                ('watering_interval', models.PositiveIntegerField(verbose_name='Watering interval')),
                ('fertilizing_interval', models.PositiveIntegerField(verbose_name='Fertilizing interval')),
                ('required_exposure', models.CharField(choices=[('dark', 'dark'), ('shade', 'shade'), ('partysun', 'part sun'), ('fullsun', 'full sun')], default='', max_length=100, verbose_name='Name')),
                ('required_temperature', models.CharField(default=False, max_length=100, verbose_name='Name')),
                ('required_humidity', models.CharField(default=False, max_length=100, verbose_name='Name')),
                ('blooming', models.BooleanField(blank=True, default=False, verbose_name='Blooming?')),
                ('difficulty', models.IntegerField(choices=[(1, 'beginner'), (2, 'medium-low'), (2, 'medium'), (2, 'medium-high'), (2, 'high')], verbose_name='')),
                ('last_watered', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Last watering')),
                ('last_fertilized', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Last fertilized')),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='plantsapp.category', verbose_name="Plant's category")),
                ('room', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='plantsapp.room', verbose_name="Plant's room")),
            ],
            options={
                'verbose_name': 'Plant',
                'verbose_name_plural': 'Plants',
            },
        ),
    ]
