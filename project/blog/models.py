from django.db import models
from tinymce import HTMLField
# Create your models here.


class Post(models.Model):
    title       = models.CharField(max_length=150, blank=True, null=True)
    image       = models.ImageField(upload_to='media/', blank=True, null=True)
    text        = HTMLField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Пости'