from django import forms

from catalog.models import Product, Version


class FormStyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.BooleanField):
                field.widget.attrs['class'] = 'form-control-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(FormStyleMixin, forms.ModelForm):

    class Meta:
        model = Product
        # fields = '__all__'
        fields = ('name', 'description', 'price', )
        # exclude = ('preview', 'created_at', 'updated_at')

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        restricted = ['казино', 'криптовалюта', 'крипта', 'биржа',
                      'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for word in restricted:
            if word in cleaned_data:
                raise forms.ValidationError('Описание не должно содержать запрещенные слова!')

        return cleaned_data


class VersionForm(FormStyleMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'
