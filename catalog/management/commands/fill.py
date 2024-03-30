from django.core.management import BaseCommand, call_command

from catalog.models import Product, Category


class Command(BaseCommand):
    def handle(self, *args, **options):

        Category.objects.all().delete()
        Product.objects.all().delete()

        call_command('loaddata', 'fixtures/catalog_data.json')
