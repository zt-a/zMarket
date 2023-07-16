from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(verbose_name='Название', max_length=100)
    slug = models.SlugField(verbose_name='URL', unique=True)

    time_create = models.DateTimeField(verbose_name='Время создание', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='Время обновление', auto_now=True)
    is_published = models.BooleanField(verbose_name='Публикация', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('categories', kwargs={'slug': self.slug})


class Product(models.Model):
    name = models.CharField(verbose_name='Название продукта', max_length=255)
    namePerson = models.CharField(verbose_name='Ваше имя', max_length=255)
    slug = models.SlugField(verbose_name='URL', unique=True)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)
    email = models.EmailField(verbose_name='Почта', max_length=255)
    phone = models.IntegerField(verbose_name='Номер телефона пр. (996701500422)')
    image = models.ImageField(verbose_name='Изображение', upload_to='product_images/photos/%Y/%m/%d/', null=True,
                              blank=True)
    video = models.FileField(verbose_name='Видео', upload_to='product_images/videos/%Y/%m/%d/', null=True, blank=True,
                             validators=[FileExtensionValidator(
                                 allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv', 'wmv', 'avi', 'flm', 'ogg'])])
    file = models.FileField(verbose_name='Документы если есть', upload_to='product_images/files/%Y/%m/%d/', null=True,
                            blank=True)

    time_create = models.DateTimeField(verbose_name='Время создание', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='Время обновление', auto_now=True)
    is_published = models.BooleanField(verbose_name='Публикация', default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class ContactUsModel(models.Model):
    name = models.CharField(verbose_name='Ваше имя', max_length=255)
    email = models.EmailField(verbose_name='Ваш Email', max_length=255)
    message = models.TextField(verbose_name='Сообщение')


    time_create = models.DateTimeField(verbose_name='Время создание', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='Время обновление', auto_now=True)
    is_published = models.BooleanField(verbose_name='Публикация', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратные связи'
        ordering = ['-time_create', 'id']