from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from reviewer_app.models import Product


# Create your views here.


class ReviewerIndexView(ListView):
    template_name = "index.html"
    model = Product
    context_object_name = "products"


class ProductDetailView(DetailView):
    template_name = "product_detailed.html"
    model = Product
    context_object_name = 'product'


# class ProductCreateView(CreateView):
#     template_name = "add_product.html"
#     model = Product
#     form_class = ProductForm
#
#     def get_success_url(self):
#         return reverse("product_detailed", kwargs={"pk": self.object.pk})



