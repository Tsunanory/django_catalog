from django.urls import path

from catalog.views import ProductListView, ProductDetailView, ProductUpdateView, ProductCreateView, ProductDeleteView

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='catalog'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product_page'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='update_product'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete_product'),
]
