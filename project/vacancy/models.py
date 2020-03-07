from django.db import models

# Create your models here.

class Vacancy(models.Model):
    country         = models.ForeignKey(to='services.Country', on_delete=models.CASCADE, blank=True, null=True, related_name='country')
    category        = models.ManyToManyField(to='Gender', blank=True, related_name='genders')
    document        = models.ForeignKey(to='DocumetType', blank=True, on_delete=models.CASCADE, null=True, related_name='documents')
    work_type       = models.ForeignKey(to='WorkType', on_delete=models.CASCADE, blank=True, null=True, related_name='work_types')
    requirements    = models.TextField(blank=True, null=True)
    work_position   = models.CharField(max_length=1000, blank=True, null=True)
    work_day        = models.CharField(max_length=1000, blank=True, null=True)
    our_duties      = models.TextField(blank=True, null=True)
    duties          = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Вакансія'
        verbose_name_plural = 'Вакансії'
    
class Gender(models.Model):
    human_type = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Стать'
        verbose_name_plural = 'Стать'
    
class DocumetType(models.Model):
    doc_type    = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Тип документів'
        verbose_name_plural = 'Тип документів'


class WorkType(models.Model):
    work_name   = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Тип роботи'
        verbose_name_plural = 'Тип роботи'