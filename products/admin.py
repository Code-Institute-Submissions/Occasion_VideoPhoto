from django.contrib import admin
from .models import Product, Category, Occasion, Package
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "get_product",
        "category",
        "occasion",
        "package",
        "price",
        "rating",
        "image",
    )

    def get_product(self, obj):
        return obj.category.friendly_name + " - " + obj.occasion.friendly_name
    get_product.admin_order_field = "name"
    get_product.short_description = 'Product Name'


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
