from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
from django.contrib.auth.models import User

class Food(models.Model):
    title = models.CharField('Название', max_length=255)
    image = models.ImageField('Изображение', blank = True, null = True)
    composition = models.CharField('Состав', max_length=150)
    description = models.CharField('Описание', max_length=150)
    price = models.DecimalField('Цена', max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = 'Еда'
        verbose_name_plural = 'Еда'

    def __str__(self):
        return self.title

class Feedback(models.Model):
    first_name = models.CharField('Имя', max_length=255, null=True)
    last_name = models.CharField('Фамилия', max_length=255, null=True)
    email = models.EmailField('Email')
    message = models.TextField('Пожелания')
    phone = models.CharField('Телефон', max_length=13) 
    date = models.DateTimeField('Дата', default= timezone.now)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

class Cookers(models.Model):
    first_name = models.CharField('Имя', max_length=255, null=True)
    last_name = models.CharField('Фамилия', max_length=255, null=True)
    image = models.ImageField('Изображение', blank = True, null = True)
    description = models.CharField('Описание', max_length=150)

    class Meta:
        verbose_name = 'Повар'
        verbose_name_plural = 'Повара'

    def __str__(self):
        return self.first_name


# py manage.py makemigrations
# py manage.py migrate