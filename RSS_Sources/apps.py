from django.apps import AppConfig
from django.db.utils import ProgrammingError

class RssSourcesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'RSS_Sources'
    verbose_name = "RSS Sources"

    def ready(self):
        try:
            from jobs import updater
            updater.start()
        except ProgrammingError as e:
            print(e)