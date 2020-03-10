from django.db import models
from tinymce import HTMLField
# Create your models here.


class Post(models.Model):
    title           = models.CharField(verbose_name='Заголовок', max_length=150, blank=True, null=True)
    image           = models.ImageField(verbose_name='Зображення', blank=True, null=True)
    text            = HTMLField(verbose_name='Текст', blank=True, null=True)
    post_category   = models.ForeignKey(verbose_name='Відноситься до категорії', to='PostCategory', blank=True, null=True, on_delete=models.CASCADE, related_name='post_categories')
    updated         = models.DateTimeField(verbose_name='Змінено', auto_now=True)

    def get_image_url(self):
        url = ''
        if self.image:
            url = self.image.url
        return url

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Пости'


class PostCategory(models.Model):
    title       = models.CharField(verbose_name='Заголовок', max_length=150, blank=True, null=True)
    slug        = models.SlugField(verbose_name='Посилання', unique=True)
    image       = models.ImageField(verbose_name='Зображення', blank=True, null=True)
    text        = HTMLField(verbose_name='Текст', blank=True, null=True)
    updated     = models.DateTimeField(verbose_name='Змінено', auto_now=True)
    def get_image_url(self):
        url = ''
        if self.image:
            url = self.image.url
        return url

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Категорія блогу'
        verbose_name_plural = 'Категорії блогу'