from django import forms
from django.core.exceptions import ValidationError

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
        fields = ('name', 'description', 'preview', 'price',)
        # exclude = ('preview', 'created_at', 'updated_at')

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        restricted = ['казино', 'криптовалюта', 'крипта', 'биржа',
                      'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for word in restricted:
            if word in cleaned_data:
                raise forms.ValidationError('Название не должно содержать запрещенные слова!')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        restricted = ['казино', 'криптовалюта', 'крипта', 'биржа',
                      'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for word in restricted:
            if word in cleaned_data:
                raise forms.ValidationError('Описание не должно содержать запрещенные слова!')

        return cleaned_data

    def clean_preview(self):
        preview = self.cleaned_data.get('preview', False)
        if preview:
            if preview.size > 4 * 1024 * 1024:
                raise ValidationError("Image file too large ( > 4mb )")
            return preview
        else:
            raise ValidationError("Couldn't read uploaded image")


class VersionForm(FormStyleMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
