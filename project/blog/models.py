from django.db import models
from tinymce import HTMLField
# Create your models here.


class Post(models.Model):
    title           = models.CharField(max_length=150, blank=True, null=True)
    image           = models.ImageField(upload_to='media/', blank=True, null=True)
    slug            = models.SlugField(unique=True)
    text            = HTMLField(blank=True, null=True)
    post_category   = models.ForeignKey(to='PostCategory', blank=True, null=True, on_delete=models.CASCADE, related_name='post_categories')

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
    title       = models.CharField(max_length=150, blank=True, null=True)
    image       = models.ImageField(upload_to='media/', blank=True, null=True)
    text        = HTMLField(blank=True, null=True)

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