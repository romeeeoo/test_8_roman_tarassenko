from django import forms

from reviewer_app.models import Product, Review


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'picture',
            'category',
        ]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            'author',
            'product',
            'review_text',
            'rate',
        ]



