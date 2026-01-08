from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple
from .models import Category, Product, Color


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ["name", "hex_code"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "slug",
        "price",
        "unit",
        "category",
        "get_colors",
        "created",
    ]
    list_editable = ["price", "unit", "category"]
    list_filter = ["category", "colors"]
    search_fields = ["name", "description"]
    prepopulated_fields = {"slug": ("name",)}
    formfield_overrides = {
        models.ManyToManyField: {"widget": CheckboxSelectMultiple},
    }

    def get_colors(self, obj):
        return ", ".join([c.name for c in obj.colors.all()])

    get_colors.short_description = "Colors"
