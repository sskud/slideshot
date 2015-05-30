from django.apps import AppConfig

class BroadcastsAppConfig(AppConfig):
    name = 'broadcasts'
    verbose_name = u'broadcasts'

    def ready(self):
        import broadcasts.handlers 