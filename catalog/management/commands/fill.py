from django.core.management import BaseCommand
from catalog.models import Category, Product
from datetime import date


class Command(BaseCommand):
    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        category_list = [
            {'name': 'Категория 1', 'description': 'описание1'},
            {'name': 'Категория 2', 'description': 'описание2'}
        ]


        for category_item in category_list:
            category = Category.objects.create(**category_item)
            self.stdout.write(self.style.SUCCESS(f'Created category: {category.name}'))

        products_list = [
            {'name': 'Продукт 1', 'description': 'Описание продукта 1', 'category': 'Категория 1', 'price': 100,
             'date_created': date.today()},
            {'name': 'Продукт 2', 'description': 'Описание продукта 2', 'category': 'Категория 2', 'price': 200,
             'date_created': date.today()},

        ]

        for product_item in products_list:
            category = Category.objects.get(name=product_item['category'])
            product_item['category'] = category
            product = Product.objects.create(**product_item)
            self.stdout.write(self.style.SUCCESS(f'Created product: {product.name}'))

        self.stdout.write(self.style.SUCCESS('Database has been filled with categories and products.'))