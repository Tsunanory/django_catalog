from django.shortcuts import render

def default(request):
    return render(request, 'catalog/index.html')