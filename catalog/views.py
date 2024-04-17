from django.views.generic import ListView, DetailView, TemplateView
from catalog.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/index.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'


class ContactsTemplateView(TemplateView):
    model = Product
    template_name = 'catalog/contacts.html'
