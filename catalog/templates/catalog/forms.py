from django import forms
from catalog.models import Product


class ProductForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')

        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']

        if name and any(word in name.lower() for word in forbidden_words):
            self.add_error('name', 'Недопустимые слова в названии продукта')

        if description and any(word in description.lower() for word in forbidden_words):
            self.add_error('description', 'Недопустимые слова в описании продукта')

    class Meta:
        model = Product
        fields = ['name', 'description', 'img', 'category', 'price', 'date_created', 'date_updated']
