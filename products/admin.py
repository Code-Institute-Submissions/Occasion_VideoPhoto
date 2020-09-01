from django.contrib import admin
from .models import Product, Category, Occasion, Package
# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Occasion)
admin.site.register(Package)


