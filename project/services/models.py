from django.db import models
from tinymce import HTMLField
# Create your models here.

class CategoryCountry(models.Model):
    title           = models.CharField(max_length=250, blank=True, null=True)
    image           = models.ImageField(upload_to='media/', blank=True, null=True)
    category        = models.ManyToManyField(to='Country', blank=True, related_name='categories')
    

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'

class Country(models.Model):
    name        = models.CharField(max_length=250, blank=True, null=True)
    slug        = models.SlugField(unique=True)
    image       = models.ImageField(upload_to='media/', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Країна'
        verbose_name_plural = 'Країни'

class StaticService(models.Model):
    title       = models.CharField(max_length=250, blank=True, null=True)
    text        = HTMLField(blank=True, null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Пости'

class CountryServices(models.Model):
    title       = models.CharField(max_length=250, blank=True, null=True)
    suptitle    = models.TextField(blank=True, null=True)
    country     = models.ForeignKey(to='Country', blank=True, null=True, on_delete=models.CASCADE, related_name='country_services')

    def __str__(self):
        return f'{self.country}, {self.title}'

    class Meta:
        verbose_name = 'Послуга'
        verbose_name_plural = 'Послуги'


class Field(models.Model):
    title       = models.CharField(max_length=250, blank=True, null=True)
    count       = HTMLField(blank=True, null=True)        
    field       = models.ForeignKey(to='CountryServices', blank=True, null=True, on_delete=models.CASCADE, related_name='fields')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Поле'
        verbose_name_plural = 'Поля'


class CategoryServices(models.Model):
    title       = models.CharField(max_length=250, blank=True, null=True)
    suptitle    = models.TextField(blank=True, null=True)
    image       = models.ImageField(upload_to='media/', blank=True, null=True)
    field       = HTMLField(blank=True, null=True)        


