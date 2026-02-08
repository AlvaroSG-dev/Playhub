from django.urls import path
from . import views

app_name = 'games'

urlpatterns = [
    path('', views.JuegoListView.as_view(), name='juego_list'),
    path('<int:pk>/', views.JuegoDetailView.as_view(), name='juego_detail'),
    path('crear/', views.JuegoCreateView.as_view(), name='juego_create'),
    path('<int:pk>/editar/', views.JuegoUpdateView.as_view(), name='juego_update'),
    path('<int:pk>/eliminar/', views.JuegoDeleteView.as_view(), name='juego_delete'),
]
