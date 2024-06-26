from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=25, verbose_name='Название')
    description = models.TextField(blank=1, null=1, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    preview = models.ImageField(upload_to='products/', verbose_name='Превью')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    salesman = models.ForeignKey(User, verbose_name='Продавец', blank=True, null=True, on_delete=models.SET_NULL)
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    def __str__(self):
        return f'{self.name} {self.category}'

    class Meta:
        permissions = [
            (
                'can_publish_продукт',
                'can_publish_продукт'
            ),
            (
                'can_change_description',
                'can change description'
            )
        ]
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    number = models.IntegerField(verbose_name='номер версии')
    name = models.CharField(max_length=30, verbose_name='название версии')
    is_current = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} {self.number}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
