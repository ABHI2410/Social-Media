from django.apps import AppConfig


class FlexispaceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'flexispace'
    # run signals when ready.
    def ready(self):
        import flexispace.signals
