from django.shortcuts import render
from catalog.models import Product, Category


def product_page(request, id):
    context = {'product': Product.objects.get(pk=id).name,
               'description': Product.objects.get(pk=id).description,
               'price': Product.objects.get(pk=id).price,
               'preview': Product.objects.get(pk=id).preview,
               }
    if not id:
        return render(request, 'catalog/index.html')
    else:
        return render(request, 'catalog/index.html', context)


def catalogue(request):
    products = Product.objects.all()
    context = {
               'object_list': products,
               }
    return render(request, 'catalog/catalogue.html', context)


def contacts(request):
    return render(request, 'catalog/contacts.html')
