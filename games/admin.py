from django.contrib import admin
from .models import Categoria, Juego


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    """
    Configuración del panel de administración para Categorías
    """
    list_display = ('nombre',)
    search_fields = ('nombre',)
    ordering = ('nombre',)


@admin.register(Juego)
class JuegoAdmin(admin.ModelAdmin):
    """
    Configuración del panel de administración para Juegos
    FASE B: Ahora incluye filter_horizontal para categorías
    """
    list_display = ('titulo', 'plataforma', 'precio', 'fecha_lanzamiento', 'get_categorias')
    search_fields = ('titulo',)
    list_filter = ('plataforma', 'fecha_lanzamiento', 'categorias')
    ordering = ('-fecha_lanzamiento',)
    filter_horizontal = ('categorias',)  # UI mejorada para ManyToMany
    
    fieldsets = (
        ('Información del Juego', {
            'fields': ('titulo', 'plataforma')
        }),
        ('Detalles', {
            'fields': ('precio', 'fecha_lanzamiento')
        }),
        ('Categorías', {
            'fields': ('categorias',)
        }),
    )
    
    def get_categorias(self, obj):
        """
        Mostrar categorías en list_display
        """
        return ", ".join([c.nombre for c in obj.categorias.all()])
    get_categorias.short_description = 'Categorías'
