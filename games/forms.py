from django import forms
from .models import Juego


class JuegoForm(forms.ModelForm):
    """
    Formulario para crear y editar juegos.
    FASE B: Ahora incluye selección de categorías (ManyToMany)
    """
    
    class Meta:
        model = Juego
        fields = ['titulo', 'plataforma', 'precio', 'fecha_lanzamiento', 'categorias']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: The Legend of Zelda'
            }),
            'plataforma': forms.Select(attrs={
                'class': 'form-control'
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 59.99',
                'step': '0.01'
            }),
            'fecha_lanzamiento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'categorias': forms.CheckboxSelectMultiple(attrs={
                'class': 'form-check-input'
            }),
        }
    
    def clean_precio(self):
        """
        Validación personalizada: el precio debe ser mayor que 0
        """
        precio = self.cleaned_data.get('precio')
        if precio is not None and precio <= 0:
            raise forms.ValidationError('El precio debe ser mayor que 0')
        return precio
