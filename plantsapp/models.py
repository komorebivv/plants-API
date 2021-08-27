from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=80,
        default='',
        unique=True,
        verbose_name='Name of category',

    )

    slug = models.SlugField(
        max_length=80,
        unique=True,
        verbose_name='Slug',

    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        app_label = 'plantsapp'


class Room(models.Model):
    name = models.CharField(
        max_length=80,
        blank=False,
        null=False,
        verbose_name='Name of Room',
        unique=True,
    )

    TEMPERATURE_CHOICE = [
        (1, 'cold'),
        (2, 'medium'),
        (3, 'warm'),
    ]

    temperature = models.IntegerField(
        choices=TEMPERATURE_CHOICE,
        verbose_name='Temperature',
        blank=False, null=False,
        help_text='',
    )

    EXPOSURE_CHOICE = (
        ('dark', 'dark'),
        ('shade', 'shade'),
        ('partysun', 'part sun'),
        ('fullsun', 'full sun'),
    )

    expose = models.CharField(
        max_length=10, choices=EXPOSURE_CHOICE,
        verbose_name="Exposure",
        help_text='',
    )

    HUMIDITY_CHOICE = [
        (1, 'low'),
        (2, 'medium'),
        (3, 'high'),
    ]

    humidity = models.CharField(
        max_length=10, choices=HUMIDITY_CHOICE,
        verbose_name="Humidity",
    )
    draft = models.BooleanField(
        blank=True,
        default=False,
        verbose_name='Draft',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'
        app_label = 'plantsapp'


class Plant(models.Model):
    name = models.CharField(
        max_length=100,
        default='',
        unique=False,
        verbose_name='Name',
    )

    category = models.ForeignKey(
        Category, on_delete=models.PROTECT,

        default=None,
        verbose_name="Plant's category",
    )
    room = models.ForeignKey(
        Room, on_delete=models.PROTECT,

        default=None,
        verbose_name="Plant's room",
    )
    watering_interval = models.PositiveIntegerField(
        verbose_name='Watering interval',
    )
    fertilizing_interval = models.PositiveIntegerField(

        verbose_name='Fertilizing interval',
    )
    required_exposure = models.CharField(
        max_length=100,
        default='',
        verbose_name='Name',
        help_text='',
        choices=Room.EXPOSURE_CHOICE,
    )

    required_temperature = models.CharField(
        max_length=100,
        default=False,
        verbose_name='Name',
        help_text='',
    )

    required_humidity = models.CharField(
        max_length=100,
        default=False,
        verbose_name='Name',
        help_text='',
    )
    blooming = models.BooleanField(
        default=False, blank=True,
        verbose_name='Blooming?',
        help_text='',
    )

    DIFFICULTY_CHOICE = (
        (1, 'beginner'),
        (2, 'medium-low'),
        (2, 'medium'),
        (2, 'medium-high'),
        (2, 'high'),
    )

    difficulty = models.IntegerField(
        blank=False, null=False,
        verbose_name='',
        choices=DIFFICULTY_CHOICE,
        help_text='',
    )

    last_watered = models.DateTimeField(
        default=None, null=True, blank=True,
        verbose_name='Last watering',
    )

    last_fertilized = models.DateTimeField(
        default=None, null=True, blank=True,
        verbose_name='Last fertilized',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Plant'
        verbose_name_plural = 'Plants'
        app_label = 'plantsapp'



