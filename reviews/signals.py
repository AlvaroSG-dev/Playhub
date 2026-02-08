from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import PerfilUsuario


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Crear automáticamente un PerfilUsuario cuando se crea un User
    """
    if created:
        PerfilUsuario.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Guardar el perfil cuando se guarda el usuario
    """
    if hasattr(instance, 'perfil'):
        instance.perfil.save()
