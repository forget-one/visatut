from django.apps import AppConfig


class ProjectConfig(AppConfig):
    name = 'project'
    verbose_name = 'Статичні сторінки'


default_app_config = 'project.ProjectConfig'

