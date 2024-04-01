from django.db import models
from django.contrib.auth.models import User


class Dish(models.Model):
    MEAL_TYPES = (
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snack', 'Snack'),
        ('other', 'Other'),
    )
    AVAILABILITY_STATUS = (
        (0, 'Available'),
        (1, 'Unavailable'),
    )

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    meal_type = models.CharField(choices=MEAL_TYPES, max_length=10)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    availability_status = models.PositiveSmallIntegerField(
        choices=AVAILABILITY_STATUS, default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
