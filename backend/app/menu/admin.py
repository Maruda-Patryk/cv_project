from django.contrib import admin

from .models import MenuCard, Dish

# Register your models here.


@admin.register(MenuCard)
class MenuCardAdmin(admin.ModelAdmin):
    list_display = ['name',]


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ['name',]