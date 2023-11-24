from django.db import models
from django.utils.text import slugify

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


    def __str__(self):
        return f'{self.name} {self.description} {self.category} {self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views_count = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  # Формируем slug из заголовка, если он не задан
        super().save(*args, **kwargs)
