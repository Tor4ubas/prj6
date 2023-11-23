from django.core.management import BaseCommand
from catalog.models import Category, Product
from datetime import date
import os
from django.conf import settings


class Command(BaseCommand):
    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        category_list = [
            {'name': 'Ноутбуки', 'description': 'Компьютеры'},
            {'name': 'Смартфоны', 'description': 'Мобильные устройства'},
            {'name': 'Телевизоры', 'description': 'Телевизоры'},
            {'name': 'Кофемашины', 'description': 'Бытовая техника'},
            {'name': 'Фитнес-трекеры', 'description': 'Гаджеты'},
        ]

        Category.objects.bulk_create([Category(**category_item) for category_item in category_list])
        self.stdout.write(self.style.SUCCESS(f'Created {len(category_list)} categories.'))

        products_list = [
            {
                "id": 1,
                "name": "Ноутбук Lenovo ThinkPad",
                "description": "Мощный ноутбук серии ThinkPad от Lenovo.",
                "img": "product/lenovo_thinkpad.jpg",
                "category": "Ноутбуки",
                "price": 1500,
                "date_created": "2022-01-01",
                "date_updated": "2022-01-10"
            },
            {
                "id": 2,
                "name": "Смартфон iPhone 12",
                "description": "Популярный смартфон от Apple с передовыми технологиями.",
                "img": "product/iphone_12.jpg",
                "category": "Смартфоны",
                "price": 1000,
                "date_created": "2022-02-01",
                "date_updated": "2022-02-15"
            },
            {
                "id": 3,
                "name": "Телевизор Samsung QLED",
                "description": "Высококачественный телевизор с технологией QLED от Samsung.",
                "img": "product/samsung_qled.jpg",
                "category": "Телевизоры",
                "price": 2000,
                "date_created": "2022-03-01",
                "date_updated": "2022-03-20"
            },
            {
                "id": 4,
                "name": "Кофемашина DeLonghi Magnifica",
                "description": "Автоматическая кофемашина для приготовления вкусного кофе.",
                "img": "product/delonghi_magnifica.jpg",
                "category": "Кофемашины",
                "price": 500,
                "date_created": "2022-04-01",
                "date_updated": "2022-04-10"
            },
            {
                "id": 5,
                "name": "Фитнес-трекер Fitbit Charge 4",
                "description": "Умный фитнес-трекер для отслеживания активности и здоровья.",
                "img": "product/fitbit_charge_4.jpg",
                "category": "Фитнес-трекеры",
                "price": 150,
                "date_created": "2022-05-01",
                "date_updated": "2022-05-05"
            }
        ]

        categories = {category.name: category for category in Category.objects.all()}
        products = [
            Product(
                name=product_item['name'],
                description=product_item['description'],
                category=categories[product_item['category']],
                price=product_item['price'],
                img=product_item['img'],
                date_created=product_item['date_created'],
                date_updated=product_item['date_updated'],
            )
            for product_item in products_list
        ]
        Product.objects.bulk_create(products)
        self.stdout.write(self.style.SUCCESS(f'Created {len(products_list)} products.'))

        self.stdout.write(self.style.SUCCESS('Database has been filled with categories and products.'))