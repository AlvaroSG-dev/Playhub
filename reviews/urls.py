from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    # Reseñas
    path('', views.ReseñaListView.as_view(), name='reseña_list'),
    path('crear/', views.ReseñaCreateView.as_view(), name='reseña_create'),
    path('<int:pk>/editar/', views.ReseñaUpdateView.as_view(), name='reseña_update'),
    path('<int:pk>/eliminar/', views.ReseñaDeleteView.as_view(), name='reseña_delete'),
    
    # Perfiles de usuario
    path('perfil/<int:pk>/', views.PerfilUsuarioDetailView.as_view(), name='perfil_detail'),
    path('perfil/editar/', views.PerfilUsuarioUpdateView.as_view(), name='perfil_edit'),
]
