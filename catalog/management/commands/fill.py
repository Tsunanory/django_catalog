from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories_to_create = [
            {
                'name': 'Сантехника',
                'description': 'Нужна в санатории'
            },
            {
                'name': 'Бытовая техника',
                'description': 'Нужна в бытовках'
            },
            {
                'name': 'Техника',
                'description': 'Нужна в техникумах'
            },
            {
                'name': 'Инструменты',
                'description': 'Без них никуда'
            },
            {
                'name': 'Музыкальные инструменты',
                'description': 'Отложены для Бременских музыкантов'
            },
        ]

        Category.objects.all().delete()

        creating_categories = []
        for cate in categories_to_create:
            creating_categories.append(Category(**cate))

        Product.objects.bulk_create(creating_categories)


class Command(BaseCommand):
    def handle(self, *args, **options):
        products_to_create = [
            {
                'name': 'Пылесос',
                'description': 'Полезный, нужный',
                'preview': 'media/vacuum.png',
                'category_id': 2,
                'price': 9999
             },
            {
                'name': 'Лопата',
                'description': 'Копает нормально',
                'preview': 'media/shovel.jpg',
                'category_id': 4,
                'price': 999
            },
            {
                'name': 'Виолончель',
                'description': 'Как она сюда попала?',
                'preview': 'media/Violin.png',
                'category': 5,
                'price': 32767
            },
            {
                'name': 'Труба',
                'description': 'Разные диаметры есть',
                'preview': 'media/Pipe.png',
                'category_id': 1,
                'price': 99
            },
            {
                'name': 'Ноутбук',
                'description': 'Их мы тоже продаем',
                'preview': 'media/Notebook.jpg',
                'category_id': 3,
                'price': 99999
            },
        ]

        Product.objects.all().delete()

        creating_products = []
        for prod in products_to_create:
            creating_products.append(Product(**prod))

        Product.objects.bulk_create(creating_products)
