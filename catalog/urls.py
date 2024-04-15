from django.urls import path

from catalog.views import catalogue

urlpatterns = [
    path('', catalogue, name='catalog'),
]
