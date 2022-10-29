from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    class Categories(models.TextChoices):
        FOOD = 'FD', _('Food')
        TOYS = 'TS', _('Toys')
        OTHER = 'OT', _('Other')
        HOME = 'HM', _('Home')

    name = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    category = models.CharField(
        max_length=2,
        null=False,
        blank=False,
        choices=Categories.choices
    )
    description = models.CharField(
        max_length=300,
        null=True,
        blank=True
    )
    picture = models.ImageField(
        null=True,
        blank=True,
        upload_to="product-picture"
    )

    def __str__(self):
        return f"{self.name}"


class Review(models.Model):
    author = models.ForeignKey(
        to=get_user_model(),
        related_name="reviews",
        on_delete=models.CASCADE,
        verbose_name="Author"
    )
    product = models.ForeignKey(
        to="reviewer_app.Product",
        related_name="reviews",
        on_delete=models.CASCADE,
        verbose_name="Product"
    )
    review_text = models.TextField(
        null=False,
        blank=False,
    )
    rate = models.PositiveIntegerField(
        validators=(
            MaxValueValidator(5),
            MinValueValidator(1))
    )

    def __str__(self):
        return f"{self.product} - {self.rate}"
