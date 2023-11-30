# Generated by Django 4.2.7 on 2023-11-30 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_version_options_remove_version_is_current_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='version',
            options={'verbose_name': 'версия', 'verbose_name_plural': 'версии'},
        ),
        migrations.AlterField(
            model_name='version',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Признак текущей версии'),
        ),
    ]