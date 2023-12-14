from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    img = models.ImageField(upload_to='product/', **NULLABLE, verbose_name='Фото')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='цена')
    date_created = models.DateField(**NULLABLE, verbose_name='Дата создания')
    date_updated = models.DateField(**NULLABLE, verbose_name='Дата последнего изменения')
    is_published = models.BooleanField(default=False)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE,
                              verbose_name='Пользователь')

    def __str__(self):
        return f'{self.name} {self.description} {self.category} {self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    version_number = models.IntegerField(verbose_name='номер версии')
    version_name = models.CharField(max_length=150, verbose_name='название версии')
    is_active = models.BooleanField(default=False, verbose_name='Признак текущей версии')
    is_current = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.product} - {self.version_name} {self.version_number}'

    def save(self, *args, **kwargs):
        if self.is_current:
            current_version = Version.objects.filter(product=self.product, is_current=True).first()
            if current_version and current_version != self:
                current_version.is_current = False
                current_version.save()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'