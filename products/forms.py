from django import forms
from .models import Product, Category, Occasion, Package


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        #model = Occasion
        #model = Package
        fields = '__all__'

    def __init__(self, *args, **kwargs): # override the init method to make a couple changes to the fields.
        super().__init__(*args, **kwargs) 

        categories = Category.objects.all()# list comprehension with shorthand way for loop that adds items to a list.
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'