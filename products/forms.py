from django import forms
from .models import Product, Category, Occasion, Package
from .widgets import CustomClearableFileInput


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)    

    def __init__(self, *args, **kwargs): # override the init method to make a couple changes to the fields.
        super().__init__(*args, **kwargs) 

        categories = Category.objects.all() # list comprehension with shorthand way for loop that adds items to a list.
        friendly_names_category = [(c.id, c.get_friendly_name()) for c in categories]

        occasions = Occasion.objects.all() # list comprehension with shorthand way for loop that adds items to a list.
        friendly_names_occasion = [(c.id, c.get_friendly_name()) for c in occasions]

        packages = Package.objects.all() # list comprehension with shorthand way for loop that adds items to a list.
        friendly_names_package = [(c.id, c.get_friendly_name()) for c in packages]

        self.fields['category'].choices = friendly_names_category
        self.fields['occasion'].choices = friendly_names_occasion
        self.fields['package'].choices = friendly_names_package



        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'