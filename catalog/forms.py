from django import forms
from catalog.models import Product, Version


class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

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
        fields = ['name', 'description', 'img', 'category', 'price',]


class VersionForm(forms.ModelForm):
    set_active = forms.BooleanField(required=False, initial=False, label='Активная версия')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Version
        fields = ['version_name', 'version_number', 'is_active']

