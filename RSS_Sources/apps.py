from django.apps import AppConfig


class RssSourcesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'RSS_Sources'
    verbose_name = "RSS Sources"

    def ready(self):
        from jobs import updater
        updater.start()
