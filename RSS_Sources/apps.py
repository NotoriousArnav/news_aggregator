from django.db.utils import ProgrammingError
from django.apps import AppConfig
# import connection

class RssSourcesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'RSS_Sources'
    verbose_name = "RSS Sources"

    def ready(self):
        # connection.close_if_unusable_or_obsolete()
        try:
            from jobs import updater
            updater.start()
        except ProgrammingError as e:
            print(e)