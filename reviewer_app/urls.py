from django.urls import path

from reviewer_app.views.product_views import ReviewerIndexView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView
from reviewer_app.views.review_views import CreateReview, UpdateReview, ReviewDeleteView

urlpatterns = [
    path('', ReviewerIndexView.as_view(), name='index'),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product_detailed"),
    path("products/add/", ProductCreateView.as_view(), name="add_product"),
    path("products/<int:pk>/update", ProductUpdateView.as_view(), name="update_product"),
    path("products/<int:pk>/delete", ProductDeleteView.as_view(), name="product_delete"),
    path("products/<int:pk>/confirm-delete", ProductDeleteView.as_view(), name="product_confirm_delete"),
    path("review/add/", CreateReview.as_view(), name="add_review"),
    path("review/<int:pk>/update", UpdateReview.as_view(), name="update_product"),
    path("review/<int:pk>/delete", ReviewDeleteView.as_view(), name="review_delete"),
    path("review/<int:pk>/confirm-delete", ReviewDeleteView.as_view(), name="review_confirm_delete"),

]
