from django.db import models
from tinymce import HTMLField
from django.urls import reverse 
from project.models import MetaData

class StaticService(models.Model):
    title           = models.CharField(verbose_name=('Заголовок'), max_length=255, blank=True, null=True)
    text            = HTMLField(verbose_name=("Підзаголовок"), blank=True, null=True)
    image           = models.ImageField(verbose_name=("Зображення"), blank=True, null=True, upload_to='static_service/')
    updated         = models.DateTimeField(verbose_name='Змінено', auto_now=True)
    
    def get_image_url(self):
        url = ''
        if self.image: url = self.image.url
        return url

    
    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = "Переглянути список послуг(без зв'язку із країнами)" 
        verbose_name_plural = "Переглянути список послуг(без зв'язку із країнами)"  


class Service(MetaData):
    title           = models.CharField(verbose_name=('Заголовок'), max_length=255, blank=True, null=True,)
    countries       = models.ForeignKey(verbose_name=("Країна"), to="service.Country", on_delete=models.CASCADE, related_name='services', blank=True, null=True)
    header          = models.TextField(verbose_name=("Підзаголовок"), blank=True, null=True, max_length=1000)
    advantages      = HTMLField(verbose_name=("Переваги"),            blank=True, null=True)
    procedure       = HTMLField(verbose_name=("Процедура відкриття"), blank=True, null=True)
    addition        = HTMLField(verbose_name=("Додаткові вимоги"),    blank=True, null=True)
    updated         = models.DateTimeField(verbose_name='Змінено', auto_now=True)

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Переглянути список послуг країн' 
        verbose_name_plural = 'Переглянути список послуг країн' 


class ServiceCategory(MetaData):
    title           = models.CharField(verbose_name=('Назва'), max_length=255, blank=True, null=True)
    image       = models.ImageField(verbose_name=("Зображення"), blank=True, null=True, upload_to='service_category/')
    updated         = models.DateTimeField(verbose_name='Змінено', auto_now=True)

    def __str__(self):
        return f'{self.title}'
    
    def get_image_url(self):
        url = ''
        if self.image: url = self.image.url
        return url
    
    class Meta:
        verbose_name = ('Переглянути категорії послуг для країн')
        verbose_name_plural = ('Переглянути категорії послуг для країн')



class Country(MetaData):
    title           = models.CharField(verbose_name=("Назва"), max_length=255, blank=True, null=True,)
    image           = models.ImageField(verbose_name=("Зображення"), blank=True, null=True, upload_to='country/')
    categories      = models.ManyToManyField(verbose_name=("Категорії послуг"), to='service.ServiceCategory', related_name='countries', blank=True)
    updated         = models.DateTimeField(verbose_name='Змінено', auto_now=True)


    def get_absolute_url(self):
        return reverse("services", kwargs={"country_pk": self.pk, 'service_category_pk': self.categories.first().id })
    
    def __str__(self):
        return f'{self.title}'

    
    def get_image_url(self):
        url = ''
        if self.image: url = self.image.url
        return url

    class Meta:
        verbose_name = 'Переглянути список країн' 
        verbose_name_plural = 'Переглянути список країн'



















