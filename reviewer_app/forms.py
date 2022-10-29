from django import forms

from reviewer_app.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'picture',
            'category',
        ]




