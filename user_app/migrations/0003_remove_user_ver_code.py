# Generated by Django 4.2.7 on 2023-12-14 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0002_alter_user_options_remove_user_code_verification_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='ver_code',
        ),
    ]
