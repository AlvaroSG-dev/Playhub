from django.db import models
from django.core.exceptions import ValidationError


class Categoria(models.Model):
    """
    Modelo para categorías de juegos (Acción, RPG, Indie, etc.)
    """
    nombre = models.CharField(max_length=100, unique=True, verbose_name='Nombre')
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre


class Juego(models.Model):
    """
    Modelo para representar un juego en el catálogo.
    FASE B: Ahora incluye relación ManyToMany con Categoría
    """
    
    PLATAFORMA_CHOICES = [
        ('PC', 'PC'),
        ('PlayStation', 'PlayStation'),
        ('Xbox', 'Xbox'),
        ('Switch', 'Switch'),
    ]
    
    titulo = models.CharField(max_length=200, verbose_name='Título')
    plataforma = models.CharField(
        max_length=20,
        choices=PLATAFORMA_CHOICES,
        verbose_name='Plataforma'
    )
    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Precio'
    )
    fecha_lanzamiento = models.DateField(verbose_name='Fecha de Lanzamiento')
    categorias = models.ManyToManyField(
        Categoria,
        blank=True,
        related_name='juegos',
        verbose_name='Categorías'
    )
    
    class Meta:
        verbose_name = 'Juego'
        verbose_name_plural = 'Juegos'
        ordering = ['-fecha_lanzamiento']
    
    def __str__(self):
        return f"{self.titulo} ({self.plataforma})"
    
    def clean(self):
        """
        Validación personalizada: el precio debe ser mayor que 0
        """
        if self.precio is not None and self.precio <= 0:
            raise ValidationError({'precio': 'El precio debe ser mayor que 0'})
