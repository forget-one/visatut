from django.db import models
from tinymce import HTMLField
from django.urls import reverse 
from project.models import MetaData

class StaticService(models.Model):
    title           = models.CharField(verbose_name='Заголовок', max_length=255, blank=True, null=True)
    text            = HTMLField(verbose_name='Підзаголовок', blank=True, null=True)
    image           = models.ImageField(verbose_name='Зображення', blank=True, null=True, upload_to='static_service/')
    updated         = models.DateTimeField(verbose_name='Змінено', auto_now=True)
    
    def get_image_url(self):
        url = ''
        if self.image: url = self.image.url
        return url

    
    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = "Послуги(без країн)" 
        verbose_name_plural = "Статичні послуги(без країн)"  


class Service(MetaData):
    title           = models.CharField(verbose_name='Заголовок', max_length=255, blank=True, null=True,)
    countries       = models.ManyToManyField(verbose_name='Країна', to="service.Country", related_name='services', blank=True)
    header          = models.TextField(verbose_name='Підзаголовок', blank=True, null=True, max_length=1000)
    advantages      = HTMLField(verbose_name='Переваги',            blank=True, null=True)
    procedure       = HTMLField(verbose_name='Процедура відкриття', blank=True, null=True)
    addition        = HTMLField(verbose_name='Додаткові вимоги',    blank=True, null=True)
    updated         = models.DateTimeField(verbose_name='Змінено', auto_now=True)

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Послуги країн' 
        verbose_name_plural = 'Послуги країн' 


class ServiceCategory(MetaData):
    title           = models.CharField(verbose_name='Назва', max_length=255, blank=True, null=True)
    image           = models.ImageField(verbose_name='Зображення', blank=True, null=True, upload_to='service_category/')
    updated         = models.DateTimeField(verbose_name='Змінено', auto_now=True)

    def __str__(self):
        return f'{self.title}'
    
    def get_image_url(self):
        url = ''
        if self.image: url = self.image.url
        return url
    
    class Meta:
        verbose_name = 'Послуги(із країнами)'
        verbose_name_plural = 'Послуги(із країнами)'



class Country(MetaData):
    title           = models.CharField(verbose_name='Назва', max_length=255, blank=True, null=True,)
    image           = models.ImageField(verbose_name='Зображення', blank=True, null=True, upload_to='country/')
    category        = models.ForeignKey(verbose_name='Категорія послуг', to='service.ServiceCategory', on_delete=models.CASCADE, related_name='country', blank=True, null=True)
    updated         = models.DateTimeField(verbose_name='Змінено', auto_now=True)


    def __str__(self):
        return f'{self.title}'

    
    def get_image_url(self):
        url = ''
        if self.image: url = self.image.url
        return url

    class Meta:
        verbose_name = 'Країни' 
        verbose_name_plural = 'Країни'



















