from django.apps import AppConfig


class ServiceConfig(AppConfig):
    name = 'project.service'
    verbose_name = 'Послуги'


default_app_config = 'project.service.ServiceConfig'