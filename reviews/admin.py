from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Reseña, PerfilUsuario


@admin.register(Reseña)
class ReseñaAdmin(admin.ModelAdmin):
    """
    Configuración del panel de administración para Reseñas
    FASE B: Ahora muestra ForeignKey a Juego y Usuario
    """
    list_display = ('get_juego', 'get_usuario', 'puntuacion', 'fecha')
    search_fields = ('juego__titulo', 'usuario__username', 'comentario')
    list_filter = ('puntuacion', 'fecha', 'juego__plataforma')
    ordering = ('-fecha',)
    readonly_fields = ('fecha',)
    
    fieldsets = (
        ('Relaciones', {
            'fields': ('juego', 'usuario')
        }),
        ('Valoración', {
            'fields': ('puntuacion', 'comentario')
        }),
        ('Metadatos', {
            'fields': ('fecha',)
        }),
    )
    
    def get_juego(self, obj):
        """
        Mostrar título del juego
        """
        return obj.juego.titulo
    get_juego.short_description = 'Juego'
    get_juego.admin_order_field = 'juego__titulo'
    
    def get_usuario(self, obj):
        """
        Mostrar nombre del usuario
        """
        return obj.usuario.username
    get_usuario.short_description = 'Usuario'
    get_usuario.admin_order_field = 'usuario__username'


@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    """
    Configuración del panel de administración para Perfiles de Usuario
    """
    list_display = ('get_username', 'plataforma_favorita')
    search_fields = ('user__username', 'bio')
    list_filter = ('plataforma_favorita',)
    ordering = ('user__username',)
    
    fieldsets = (
        ('Usuario', {
            'fields': ('user',)
        }),
        ('Información del Perfil', {
            'fields': ('bio', 'plataforma_favorita', 'avatar_url')
        }),
    )
    
    def get_username(self, obj):
        """
        Mostrar nombre de usuario
        """
        return obj.user.username
    get_username.short_description = 'Usuario'
    get_username.admin_order_field = 'user__username'


# Inline para mostrar el perfil en el admin de User
class PerfilUsuarioInline(admin.StackedInline):
    """
    Inline para editar el perfil desde el admin de User
    """
    model = PerfilUsuario
    can_delete = False
    verbose_name_plural = 'Perfil'
    fk_name = 'user'
    fields = ('bio', 'plataforma_favorita', 'avatar_url')


# Extender el UserAdmin para incluir el perfil
class UserAdmin(BaseUserAdmin):
    """
    Admin personalizado para User que incluye el perfil inline
    """
    inlines = (PerfilUsuarioInline,)


# Desregistrar el UserAdmin original y registrar el personalizado
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
