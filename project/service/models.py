from django.db import models
from tinymce import HTMLField
from django.urls import reverse 
from project.models import MetaData

class StaticService(models.Model):
    title           = models.CharField(verbose_name=('Заголовок'), max_length=255)
    text            = HTMLField(verbose_name=("Текст"), blank=True, null=True)
    image           = models.ImageField(verbose_name=("Зображення"), blank=True, null=True, upload_to='static_service/')
    
    def get_image_url(self):
        url = ''
        if self.image: url = self.image.url
        return url

    
    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Сервіс' 
        verbose_name_plural = 'Сервіси' 


class Service(MetaData):
    title           = models.CharField(verbose_name=('Заголовок'), max_length=255)
    categories      = models.ManyToManyField(verbose_name=("Категорії послуги"), to="service.ServiceCategory", related_name='services')
    countries       = models.ManyToManyField(verbose_name=("Країни"), to="service.Country",         related_name='services')
    header          = models.TextField(verbose_name=("Підзаголовок"), blank=True, null=True, max_length=1000)
    advantages      = HTMLField(verbose_name=("Переваги"),            blank=True, null=True)
    procedure       = HTMLField(verbose_name=("Процедура відкриття"), blank=True, null=True)
    addition        = HTMLField(verbose_name=("Додаткові вимоги"),    blank=True, null=True)

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Сервіс по країнах' 
        verbose_name_plural = 'Сервіси по країнах' 


class ServiceCategory(MetaData):
    title           = models.CharField(verbose_name=('Назва'), max_length=255, blank=True, null=True)
    image       = models.ImageField(verbose_name=("Зображення"), blank=True, null=True, upload_to='service_category/')

    def __str__(self):
        return f'{self.title}'
    
    def get_image_url(self):
        url = ''
        if self.image: url = self.image.url
        return url
    
    class Meta:
        verbose_name = ('Категорія сервісу')
        verbose_name_plural = ('Категорія сервісу')



class Country(MetaData):
    title           = models.CharField(verbose_name=("Назва"), max_length=255)
    image           = models.ImageField(verbose_name=("Зображення"), blank=True, null=True, upload_to='country/')
    categories      = models.ManyToManyField(verbose_name=("Категорії"), to='service.ServiceCategory', related_name='countries', blank=False)


    def get_absolute_url(self):
        return reverse("services", kwargs={"country_pk": self.pk, 'service_category_pk': self.categories.first().id })
    
    def __str__(self):
        return f'{self.title}'

    
    def get_image_url(self):
        url = ''
        if self.image: url = self.image.url
        return url

    class Meta:
        verbose_name = 'Країна' 
        verbose_name_plural = 'Країни'



















