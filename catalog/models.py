from django.db import models
from datetime import date

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
    preview = models.ImageField(blank=True, null=True, verbose_name='Превью')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, verbose_name='Категория')
    price = models.SmallIntegerField(verbose_name='Цена')
    manufactured_at = models.DateField(default=date(year=2024, month=1, day=1), verbose_name='Дата производства')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return f'{self.name} {self.category}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
