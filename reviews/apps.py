from django.apps import AppConfig


class ReviewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reviews'
    verbose_name = 'Reseñas'
    
    def ready(self):
        """
        Importar signals cuando la app esté lista
        """
        import reviews.signals
