from django.apps import AppConfig


class MainConfig(AppConfig):
    name = 'main'

    def ready(self):
        super().ready()
        from .receivers import send_email_notification
