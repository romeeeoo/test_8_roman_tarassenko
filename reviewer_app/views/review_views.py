from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from reviewer_app.forms import ReviewForm
from reviewer_app.models import Review


class CreateReview(CreateView):
    template_name = "review/add_review.html"
    model = Review
    form_class = ReviewForm

    def post(self, request, *args, **kwargs):
        form = self.get_form_class()(request.POST)
        if form.is_valid():
            user = request.user
            product = form.cleaned_data.get('product')
            review_text = form.cleaned_data.get('review_text')
            rate = form.cleaned_data.get('rate')
            if not Review.objects.filter(user=user, product=product).exists():
                Review.objects.create(user=user, product=product, review_text=review_text, rate=rate)
            return redirect('index')

    def get_success_url(self):
        return reverse("index")


class UpdateReview(UpdateView):
    template_name = "review/update_review.html"
    model = Review
    form_class = ReviewForm

    def get_success_url(self):
        return reverse("index")


class ReviewDeleteView(DeleteView):
    template_name = "review/review_confirm_delete.html"
    model = Review
    success_url = reverse_lazy("index")
