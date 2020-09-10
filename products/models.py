from django.db import models

# Create your models here.


class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name     


class Occasion(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name    


class Package(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    occasion = models.ForeignKey('Occasion', null=True, blank=True, on_delete=models.SET_NULL)
    package = models.ForeignKey('Package', null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField()
    things_include = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.category.name + " - " + self.occasion.name

    def thingsInclude_as_list(self):
        return self.things_include.split(',')

    def get_name_categoryOccasion(self):
        return self.category.friendly_name + " " + self.occasion.friendly_name

    def get_shortDescription(self):
        return self.long_description[:100]
