from django.contrib import admin
from .models import Product, Category, Philosopher, ShirtsReview


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'philosopher',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class PhilosopherAdmin(admin.ModelAdmin):
    list_display = (
         "friendly_name",
         "name",
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Philosopher, PhilosopherAdmin)
admin.site.register(ShirtsReview)
