from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from reviewer_app.forms import ProductForm
from reviewer_app.models import Product, Review


# Create your views here.


class ReviewerIndexView(ListView):
    template_name = "product/index.html"
    model = Product
    context_object_name = "products"





class ProductDetailView(DetailView):
    template_name = "product/product_detailed.html"
    model = Product
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_reviews = Review.objects.filter(product=self.get_object())
        if len(product_reviews) != 0:
            review_sum = 0
            for i in product_reviews:
               review_sum += i.rate
            avg_rate = review_sum/len(product_reviews)
            context["avg_rate"] = avg_rate
        return super().get_context_data(**context)


class ProductCreateView(CreateView):
    template_name = "product/add_product.html"
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse("product_detailed", kwargs={"pk": self.object.pk})


class ProductUpdateView(UpdateView):
    template_name = "product/update_product.html"
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse("product_detailed", kwargs={"pk": self.object.pk})


class ProductDeleteView(DeleteView):
    template_name = "product/product_confirm_delete.html"
    model = Product
    success_url = reverse_lazy("index")





