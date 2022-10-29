from django.urls import path

from reviewer_app.views import ReviewerIndexView, ProductDetailView

urlpatterns = [
    path('', ReviewerIndexView.as_view(), name='index'),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product_detailed"),

]
