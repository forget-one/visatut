from django.db import models
from tinymce import HTMLField
from django.urls import reverse
from project.models import MetaData
# Create your models here.

class Post(MetaData):
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Пости'

    title           = models.CharField( verbose_name='Заголовок', max_length=150, blank=True, null=True)
    image           = models.ImageField(verbose_name='Зображення', blank=True, null=True)
    text            = HTMLField(verbose_name='Текст', blank=True, null=True)
    category        = models.ForeignKey(verbose_name='Відноситься до категорії', to='PostCategory', blank=True, null=True, on_delete=models.CASCADE, related_name='posts')
    updated         = models.DateTimeField(verbose_name='Змінено', auto_now=True)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse("post", kwargs={"id": self.pk})

    def get_image_url(self):
        url = ''
        if self.image: url = self.image.url
        return url


class PostCategory(MetaData):
    class Meta:
        verbose_name = 'Категорію блогу'
        verbose_name_plural = 'Категорії блогу'

    title           = models.CharField(verbose_name='Заголовок', max_length=150, blank=True, null=True)
    slug            = models.SlugField(verbose_name='Посилання', unique=True)
    image           = models.ImageField(verbose_name='Зображення', blank=True, null=True)
    updated         = models.DateTimeField(verbose_name='Змінено', auto_now=True)

    def __str__(self):
        return f'{self.title}'
        
    def get_absolute_url(self):
        return reverse('blog', kwargs={'slug': self.slug})

    def get_image_url(self):
        url = ''
        if self.image: url = self.image.url
        return url
