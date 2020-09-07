from django.contrib import admin
from .models import Product, Category, Occasion, Package
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "category",
        "occasion",
        "package",
        "price",
        "rating",
        "image",
    )
    ordering = ("category",)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "friendly_name",
        "name",
    )


class OccasionAdmin(admin.ModelAdmin):
    list_display = (
        "friendly_name",
        "name",
    )


class PackageAdmin(admin.ModelAdmin):
    list_display = (
        "friendly_name",
        "name",
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Occasion, OccasionAdmin)
admin.site.register(Package, PackageAdmin)


