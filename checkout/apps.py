from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

# Importing signals to save order total
    def ready(self):
        import checkout.signals
