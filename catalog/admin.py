from django.contrib import admin
from catalog.models import Product, Category


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ('id', 'name', )
    list_filter = ('name', )

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', )
    search_fields = ('name', 'description', )
    list_filter = ('category', )
