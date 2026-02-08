from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Avg
from .models import Juego
from .forms import JuegoForm


class JuegoListView(ListView):
    """
    Vista para listar todos los juegos
    """
    model = Juego
    template_name = 'games/juego_list.html'
    context_object_name = 'juegos'
    paginate_by = 12


class JuegoDetailView(DetailView):
    """
    Vista para mostrar los detalles de un juego.
    FASE B: Ahora incluye reseñas relacionadas y categorías
    RETO OPCIONAL: Calcula la media de puntuación con ORM
    """
    model = Juego
    template_name = 'games/juego_detail.html'
    context_object_name = 'juego'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtener reseñas relacionadas con este juego
        context['reseñas'] = self.object.reseñas.all().select_related('usuario')
        # Calcular puntuación promedio usando agregación de Django ORM
        puntuacion_avg = self.object.reseñas.aggregate(Avg('puntuacion'))['puntuacion__avg']
        context['puntuacion_promedio'] = round(puntuacion_avg, 1) if puntuacion_avg else None
        context['total_reseñas'] = self.object.reseñas.count()
        return context


class JuegoCreateView(CreateView):
    """
    Vista para crear un nuevo juego
    """
    model = Juego
    form_class = JuegoForm
    template_name = 'games/juego_form.html'
    success_url = reverse_lazy('games:juego_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_pagina'] = 'Agregar Juego'
        return context


class JuegoUpdateView(UpdateView):
    """
    Vista para editar un juego existente
    """
    model = Juego
    form_class = JuegoForm
    template_name = 'games/juego_form.html'
    success_url = reverse_lazy('games:juego_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_pagina'] = 'Editar Juego'
        return context


class JuegoDeleteView(DeleteView):
    """
    Vista para eliminar un juego
    """
    model = Juego
    template_name = 'games/juego_confirm_delete.html'
    success_url = reverse_lazy('games:juego_list')
    context_object_name = 'juego'
