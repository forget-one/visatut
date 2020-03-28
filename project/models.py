from django.db import models


class Page(models.Model):
    class Meta:
        verbose_name = 'Сторінки'
        verbose_name_plural = 'Сторінки'

    title       = models.CharField(verbose_name='Мета-заголовок', max_length=255, blank=True, null=True)
    slug        = models.CharField(verbose_name='URL', max_length=255, unique=True)
    meta_descr  = models.TextField(verbose_name="Мета-опис", blank=True, null=True)
    meta_key    = models.TextField(verbose_name="Ключові слова", blank=True, null=True)

    def __str__(self):
        return f'{self.title} --- {self.slug}'

    def get_absolute_url(self):
        return f'{self.slug}'


class MetaData(models.Model):
    class Meta:
        abstract = True

    meta_title      = models.CharField(verbose_name='Мета-заголовок', max_length=255, blank=True, null=True)
    meta_descr      = models.TextField(verbose_name="Мета-опис", blank=True, null=True)
    meta_key        = models.TextField(verbose_name="Мета-ключі", blank=True, null=True)
