from django.urls import path

from catalog.views import catalogue

urlpatterns = [
    path('catalog/', catalogue, name='catalog'),
]
