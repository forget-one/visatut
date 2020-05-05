from django.apps import AppConfig


class FeedbackConfig(AppConfig):
    name = 'project.feedback'
    verbose_name = 'Зворотній зв\'язок'


default_app_config = 'project.feedback.FeedbackConfig'
