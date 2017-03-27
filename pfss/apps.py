from django.apps import AppConfig as BaseAppConfig
#from django.utils.importlib import import_module
from importlib import import_module


class AppConfig(BaseAppConfig):

    name = "pfss"

    def ready(self):
        import_module("pfss.receivers")
