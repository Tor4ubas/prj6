from django.core.management import BaseCommand

from user_app.models import User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        user = User.objects.create(
            email='alex1029@yandex.ru',
            first_name='admin',
            last_name='admin',

            is_staff=True,
            is_superuser=True
        )

        user.set_password('admin')
        user.save()
