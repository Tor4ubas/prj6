from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):
    help = 'Clear data in the database'
    def handle(self, *args, **options):
        Category.objects.all().delete()
        category1 = Category(name='Category 1')
        category1.save()
        self.stdout.write(self.style.SUCCESS('Data clear successfully.'))



