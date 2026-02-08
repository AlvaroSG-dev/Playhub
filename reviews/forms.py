from django import forms
from .models import Reseña, PerfilUsuario


class ReseñaForm(forms.ModelForm):
    """
    Formulario para crear y editar reseñas.
    FASE B: Ahora usa ForeignKey para seleccionar el juego.
    El usuario se asigna automáticamente desde request.user
    """
    
    class Meta:
        model = Reseña
        fields = ['juego', 'puntuacion', 'comentario']
        widgets = {
            'juego': forms.Select(attrs={
                'class': 'form-control'
            }),
            'puntuacion': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1',
                'max': '10',
                'placeholder': 'Puntuación (1-10)'
            }),
            'comentario': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Escribe tu reseña aquí (mínimo 50 caracteres)...'
            }),
        }
    
    def clean_puntuacion(self):
        """
        Validación personalizada: la puntuación debe estar entre 1 y 10
        """
        puntuacion = self.cleaned_data.get('puntuacion')
        if puntuacion is not None:
            if puntuacion < 1 or puntuacion > 10:
                raise forms.ValidationError('La puntuación debe estar entre 1 y 10')
        return puntuacion
    
    def clean_comentario(self):
        """
        Validación personalizada: el comentario debe tener al menos 50 caracteres
        """
        comentario = self.cleaned_data.get('comentario')
        if comentario and len(comentario) < 50:
            raise forms.ValidationError(
                f'El comentario debe tener al menos 50 caracteres. '
                f'Actualmente tiene {len(comentario)} caracteres.'
            )
        return comentario


class PerfilUsuarioForm(forms.ModelForm):
    """
    Formulario para editar el perfil de usuario.
    El campo user se asigna automáticamente.
    """
    
    class Meta:
        model = PerfilUsuario
        fields = ['bio', 'plataforma_favorita', 'avatar_url']
        widgets = {
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Cuéntanos sobre ti y tus gustos en videojuegos...'
            }),
            'plataforma_favorita': forms.Select(attrs={
                'class': 'form-control'
            }),
            'avatar_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://ejemplo.com/avatar.jpg'
            }),
        }
