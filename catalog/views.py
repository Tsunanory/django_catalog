from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView, TemplateView

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


# def contacts(request):
#     return render(request, 'catalog/contacts.html')
