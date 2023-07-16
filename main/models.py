from django.db import models

class Category(models.Model):
    name = models.CharField(verbose_name='Название', max_length=100)
    slug = models.SlugField(verbose_name='URL', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(verbose_name='Название', max_length=100)
    slug = models.SlugField(verbose_name='URL', unique=True)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)
    image = models.ImageField(verbose_name='Изображение', upload_to='product_images')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
