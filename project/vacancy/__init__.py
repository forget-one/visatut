from django.apps import AppConfig


class VacancyConfig(AppConfig):
    name = 'project.vacancy'
    verbose_name = 'Пошук роботи'
    

default_app_config = 'project.vacancy.VacancyConfig'

