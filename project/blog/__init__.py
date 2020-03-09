from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'project.blog'
    verbose_name = 'Блог'


default_app_config = 'project.blog.BlogConfig'
