from django.shortcuts import render
from catalog.models import *


def product_page(request, id):
    if not id:
        return render(request, 'catalog/index.html')
    else:
        return render(request, 'catalog/index.html',
                      {'product': Product.objects.get(pk=id).name,
                       'description': Product.objects.get(pk=id).description,
                       'price': Product.objects.get(pk=id).price,
                       'preview': Product.objects.get(pk=id).preview})

