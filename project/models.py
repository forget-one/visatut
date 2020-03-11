from django.db import models



class Page(models.Model):
    title = models.CharField(verbose_name='Назва', max_length=100, blank=True, null=True)
    code  = models.CharField(verbose_name='URL', max_length=255, unique=True)

    def __str__(self):
        return f'{self.title} --- {self.code}'

    class Meta:
        verbose_name = 'Сторінка'
        verbose_name_plural = 'Сторінки'