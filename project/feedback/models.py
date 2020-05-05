from django.db import models

# Create your models here.
class Supprot(models.Model):
  class Meta:
    verbose_name = 'Клієнт'
    verbose_name_plural = 'Клієнти'
    
  name    = models.CharField(verbose_name='Ім\'я', max_length=100, blank=True, null=True)
  phone   = models.CharField(verbose_name='Телефон', max_length=100, blank=True, null=True)
  descr   = models.CharField(verbose_name='Електронний адрес', max_length=100, blank=True, null=True)
  
  added   = models.DateTimeField(verbose_name='Змінено', auto_now_add=True)

  def __str__(self):
    return f'{self.name} {self.phone}'

