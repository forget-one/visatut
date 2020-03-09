from django.apps import AppConfig


class ServiceConfig(AppConfig):
    name = 'project.service'
    verbose_name = 'Сервіс'


default_app_config = 'project.service.ServiceConfig'