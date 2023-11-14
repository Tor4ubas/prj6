from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):
    help = 'Clear data in the database'
    def handle(self, *args, **options):
        Category.objects.all().delete()
        category_list = [
            {'name': 'название1', 'description': 'описание1'},
            {'name': 'название2', 'description': 'описание2'}

        ]
        category_for_create = []
        for category_item in category_list:
            category_for_create.append(
                Category(**category_item)
            )
        Category.objects.bulk_create(category_for_create)
        self.stdout.write(self.style.SUCCESS('Data clear successfully.'))



