from django.urls import path

from catalog.views import ProductListView, ProductDetailView

urlpatterns = [
    path('', ProductListView.as_view(), name='catalog'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product_page'),
]
