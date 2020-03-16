from django.db import models

# Create your models here.

class Vacancy(models.Model):
    name            = models.CharField(verbose_name='Назва роботи', max_length=150, blank=True, null=True)
    country         = models.ForeignKey(to='service.Country', verbose_name='Країна', on_delete=models.CASCADE, blank=True, null=True, related_name='country')
    gender          = models.ForeignKey(to='Gender', verbose_name='Робота для',  blank=True, null=True, on_delete=models.CASCADE)
    document        = models.ForeignKey(to='DocumetType', verbose_name='Необхідні документи', blank=True, on_delete=models.CASCADE, null=True, related_name='documents')
    work_type       = models.ForeignKey(to='WorkType', verbose_name='Місце роботи', on_delete=models.CASCADE, blank=True, null=True, related_name='work_types')
    requirements    = models.TextField(verbose_name='Вимоги', blank=True, null=True)
    work_position   = models.CharField(verbose_name='Адреса роботи', max_length=1000, blank=True, null=True)
    work_day        = models.CharField(verbose_name='Графік роботи', max_length=1000, blank=True, null=True)
    your_duties     = models.TextField(verbose_name='Витрати працівників', blank=True, null=True)
    our_duties      = models.TextField(verbose_name='Компанія надає', blank=True, null=True)
    duties          = models.TextField(verbose_name="Обов'язки", blank=True, null=True)
    actual          = models.BooleanField(verbose_name="Актуальна?", default=True)
    meta_title      = models.CharField(verbose_name='Мета-заголовок', max_length=255, blank=True, null=True)
    meta_descr      = models.TextField(verbose_name=("Мета-опис"), blank=True, null=True)
    meta_key        = models.TextField(verbose_name=("Мета-ключі"), blank=True, null=True)
    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Вакансія'
        verbose_name_plural = 'Вакансії'
    
class Gender(models.Model):
    human_type = models.CharField(verbose_name="Обов'язки", max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.human_type}'

    class Meta:
        verbose_name = 'Робота для'
        verbose_name_plural = 'Робота для'
    
class DocumetType(models.Model):
    doc_type    = models.CharField(verbose_name="Необхідні документи", max_length=50, blank=True, null=True)
    description = models.CharField(verbose_name="Опис необхідних документів", max_length=300, blank=True, null=True)

    def __str__(self):
        return f'{self.doc_type}'

    class Meta:
        verbose_name = 'Необхідні документи'
        verbose_name_plural = 'Необхідні документи'


class WorkType(models.Model):
    work_type   = models.CharField(verbose_name="Тип роботи", max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.work_type}'

    class Meta:
        verbose_name = 'Тип роботи'
        verbose_name_plural = 'Тип роботи'