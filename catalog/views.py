from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView

from catalog.models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/index.html'

# def catalogue(request):
#     products = Product.objects.all()
#     context = {
#                'object_list': products,
#                }
#     return render(request, 'catalog/index.html', context)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'

# def product_page(request, id):
#     prod = get_object_or_404(Product, pk=id)
#     context = {'product': prod.name,
#                'description': prod.description,
#                'category': prod.category,
#                'price': prod.price,
#                'preview': prod.preview,
#                }
#     return render(request, 'catalog/product.html', context)


def contacts(request):
    return render(request, 'catalog/contacts.html')
