from django.db import models
from tinymce import HTMLField
from django.urls import reverse 
from project.models import MetaData

class StaticService(models.Model):
    class Meta:
        verbose_name = "Послугу без прив'язки до країни" 
        verbose_name_plural = "Послуги без прив'язки до країн"  

    title           = models.CharField(verbose_name='Заголовок', max_length=255, blank=True, null=True)
    text            = HTMLField(verbose_name='Підзаголовок', blank=True, null=True)
    image           = models.ImageField(verbose_name='Зображення', blank=True, null=True, upload_to='static_service/')
    updated         = models.DateTimeField(verbose_name='Змінено', auto_now=True)
    
    def __str__(self):
        return f'{self.title}'

    def get_image_url(self):
        url = ''
        if self.image: url = self.image.url
        return url
    

class Service(MetaData):
    class Meta:
        verbose_name = 'Сервіс' 
        verbose_name_plural = 'Сервіси' 

    title           = models.CharField(verbose_name='Заголовок', max_length=255, blank=True, null=True,)
    country         = models.ForeignKey(verbose_name='Країна', to="service.Country", on_delete=models.CASCADE, related_name='services', blank=True, null=True)
    header          = models.TextField(verbose_name='Підзаголовок', blank=True, null=True, max_length=1000)
    advantages      = HTMLField(verbose_name='Переваги',            blank=True, null=True)
    procedure       = HTMLField(verbose_name='Процедура відкриття', blank=True, null=True)
    addition        = HTMLField(verbose_name='Додаткові вимоги',    blank=True, null=True)
    updated         = models.DateTimeField(verbose_name='Змінено', auto_now=True)

    def __str__(self):
        return f'{self.title} --- {self.country}'

    def get_absolute_url(self):
        return reverse("service", kwargs={"service_id": self.pk})
    

class ServiceCategory(MetaData):
    class Meta:
        verbose_name = 'Категорію сервісу'
        verbose_name_plural = 'Категорії сервісів'

    title           = models.CharField(verbose_name='Назва', max_length=255, blank=True, null=True)
    image           = models.ImageField(verbose_name='Зображення', blank=True, null=True, upload_to='service_category/')
    updated         = models.DateTimeField(verbose_name='Змінено', auto_now=True)

    def __str__(self):
        return f'{self.title}'
    
    def get_image_url(self):
        url = ''
        if self.image: url = self.image.url
        return url


class Country(MetaData):
    class Meta:
        verbose_name = 'Країну' 
        verbose_name_plural = 'Країни'

    title           = models.CharField(verbose_name='Назва', max_length=255, blank=True, null=True,)
    image           = models.ImageField(verbose_name='Зображення', blank=True, null=True, upload_to='country/')
    category        = models.ForeignKey(verbose_name='Категорія послуг', to='service.ServiceCategory', on_delete=models.CASCADE, related_name='country', blank=True, null=True)
    updated         = models.DateTimeField(verbose_name='Змінено', auto_now=True)

    def __str__(self):
        return f'{self.title} --- {self.category}'

    def get_absolute_url(self):
        return reverse("services", kwargs={"country_pk": self.pk})
    
    def get_image_url(self):
        url = ''
        if self.image: url = self.image.url
        return url
