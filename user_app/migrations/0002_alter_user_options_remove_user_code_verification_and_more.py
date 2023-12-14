# Generated by Django 4.2.7 on 2023-12-14 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.RemoveField(
            model_name='user',
            name='code_verification',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_verified',
        ),
        migrations.AddField(
            model_name='user',
            name='email_verification',
            field=models.BooleanField(default=False, verbose_name='Верификация почты'),
        ),
        migrations.AddField(
            model_name='user',
            name='ver_code',
            field=models.CharField(default='655235036862', max_length=15, verbose_name='Проверочный код'),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(upload_to='user_app/', verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Активность'),
        ),
        migrations.AlterModelTable(
            name='user',
            table=None,
        ),
    ]