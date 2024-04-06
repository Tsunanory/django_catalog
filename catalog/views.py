from django.shortcuts import render, get_object_or_404
from catalog.models import Product, Category


def product_page(request, id):
    # prod = Product.objects.get(pk=id)
    prod = get_object_or_404(Product, pk=id)
    context = {'product': prod.name,
               'description': prod.description,
               'category': prod.category,
               'price': prod.price,
               'preview': prod.preview,
               }
    return render(request, 'catalog/index.html', context)


def catalogue(request):
    products = Product.objects.all()
    context = {
               'object_list': products,
               }
    return render(request, 'catalog/catalogue.html', context)


def contacts(request):
    return render(request, 'catalog/contacts.html')
