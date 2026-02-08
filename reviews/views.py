from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import Reseña, PerfilUsuario
from .forms import ReseñaForm, PerfilUsuarioForm


class ReseñaListView(ListView):
    """
    Vista para listar todas las reseñas
    """
    model = Reseña
    template_name = 'reviews/reseña_list.html'
    context_object_name = 'reseñas'
    paginate_by = 10
    
    def get_queryset(self):
        # Optimizar consultas con select_related
        return Reseña.objects.all().select_related('juego', 'usuario')


class ReseñaCreateView(LoginRequiredMixin, CreateView):
    """
    Vista para crear una nueva reseña.
    Requiere autenticación y asigna automáticamente el usuario (FK).
    """
    model = Reseña
    form_class = ReseñaForm
    template_name = 'reviews/reseña_form.html'
    success_url = reverse_lazy('reviews:reseña_list')
    
    def form_valid(self, form):
        # Asignar automáticamente el usuario autenticado (ForeignKey)
        form.instance.usuario = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_pagina'] = 'Crear Reseña'
        return context


class ReseñaUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Vista para editar una reseña existente.
    Requiere autenticación y solo el autor puede editar.
    """
    model = Reseña
    form_class = ReseñaForm
    template_name = 'reviews/reseña_form.html'
    success_url = reverse_lazy('reviews:reseña_list')
    
    def test_func(self):
        """
        Verificar que el usuario actual es el autor de la reseña
        """
        reseña = self.get_object()
        return self.request.user == reseña.usuario
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_pagina'] = 'Editar Reseña'
        return context


class ReseñaDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Vista para eliminar una reseña.
    Requiere autenticación y solo el autor puede eliminar.
    """
    model = Reseña
    template_name = 'reviews/reseña_confirm_delete.html'
    success_url = reverse_lazy('reviews:reseña_list')
    context_object_name = 'reseña'
    
    def test_func(self):
        """
        Verificar que el usuario actual es el autor de la reseña
        """
        reseña = self.get_object()
        return self.request.user == reseña.usuario


class PerfilUsuarioDetailView(DetailView):
    """
    Vista para mostrar el perfil de un usuario
    """
    model = PerfilUsuario
    template_name = 'reviews/perfil_detail.html'
    context_object_name = 'perfil'
    
    def get_object(self):
        """
        Obtener el perfil del usuario especificado
        """
        user = get_object_or_404(User, pk=self.kwargs['pk'])
        # Crear perfil si no existe (por si acaso)
        perfil, created = PerfilUsuario.objects.get_or_create(user=user)
        return perfil
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtener reseñas del usuario
        context['reseñas_usuario'] = self.object.user.reseñas.all().select_related('juego')
        return context


class PerfilUsuarioUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Vista para editar el perfil de usuario.
    Solo el propio usuario puede editar su perfil.
    """
    model = PerfilUsuario
    form_class = PerfilUsuarioForm
    template_name = 'reviews/perfil_form.html'
    
    def test_func(self):
        """
        Verificar que el usuario está editando su propio perfil
        """
        perfil = self.get_object()
        return self.request.user == perfil.user
    
    def get_object(self):
        """
        Obtener el perfil del usuario actual
        """
        perfil, created = PerfilUsuario.objects.get_or_create(user=self.request.user)
        return perfil
    
    def get_success_url(self):
        return reverse_lazy('reviews:perfil_detail', kwargs={'pk': self.request.user.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_pagina'] = 'Editar Perfil'
        return context
