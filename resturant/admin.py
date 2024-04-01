from django.contrib import admin
from .models import Dish


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'meal_type')
    list_filter = ('meal_type',)
    search_fields = ('name',)

    fieldsets = (
        (None, {'fields': ('name', 'price', 'meal_type')}),
        ('Author', {'fields': ('author',)}),
        ('Availability', {'fields': ('availability_status',)}),
        ('Meta data', {'fields': ('date_created', 'date_updated')}),
    )

    readonly_fields = ('date_created', 'date_updated')
