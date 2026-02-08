from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from games.models import Juego


class Reseña(models.Model):
    """
    Modelo para representar una reseña de un juego.
    FASE B: Ahora usa ForeignKey para relacionar con Juego y User
    """
    
    juego = models.ForeignKey(
        Juego,
        on_delete=models.CASCADE,
        related_name='reseñas',
        verbose_name='Juego'
    )
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reseñas',
        verbose_name='Usuario'
    )
    puntuacion = models.IntegerField(verbose_name='Puntuación')
    comentario = models.TextField(verbose_name='Comentario')
    fecha = models.DateTimeField(auto_now_add=True, verbose_name='Fecha')
    
    class Meta:
        verbose_name = 'Reseña'
        verbose_name_plural = 'Reseñas'
        ordering = ['-fecha']
        # Evitar que un usuario reseñe el mismo juego múltiples veces
        unique_together = ['juego', 'usuario']
    
    def __str__(self):
        return f"Reseña de {self.usuario.username} para {self.juego.titulo}"
    
    def clean(self):
        """
        Validaciones personalizadas:
        - La puntuación debe estar entre 1 y 10
        - El comentario debe tener al menos 50 caracteres
        """
        if self.puntuacion is not None:
            if self.puntuacion < 1 or self.puntuacion > 10:
                raise ValidationError({
                    'puntuacion': 'La puntuación debe estar entre 1 y 10'
                })
        
        if self.comentario and len(self.comentario) < 50:
            raise ValidationError({
                'comentario': 'El comentario debe tener al menos 50 caracteres'
            })


class PerfilUsuario(models.Model):
    """
    Modelo para extender el User de Django con información adicional.
    Relación OneToOne con User.
    """
    
    PLATAFORMA_CHOICES = [
        ('PC', 'PC'),
        ('PlayStation', 'PlayStation'),
        ('Xbox', 'Xbox'),
        ('Switch', 'Switch'),
        ('Múltiples', 'Múltiples Plataformas'),
    ]
    
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='perfil',
        verbose_name='Usuario'
    )
    bio = models.TextField(
        blank=True,
        verbose_name='Biografía',
        help_text='Cuéntanos sobre ti y tus gustos en videojuegos'
    )
    plataforma_favorita = models.CharField(
        max_length=20,
        choices=PLATAFORMA_CHOICES,
        default='PC',
        verbose_name='Plataforma Favorita'
    )
    avatar_url = models.URLField(
        blank=True,
        verbose_name='URL del Avatar',
        help_text='URL de tu imagen de perfil'
    )
    
    class Meta:
        verbose_name = 'Perfil de Usuario'
        verbose_name_plural = 'Perfiles de Usuario'
    
    def __str__(self):
        return f"Perfil de {self.user.username}"
