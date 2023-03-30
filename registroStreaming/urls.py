from django.urls import path
from . import views
from .views import ServicioListView, ServicioCreateView, ServicioUpdateView, ServicioDeleteView, ServicioProximosView, servicio_pago


urlpatterns = [
    path('', ServicioListView.as_view(), name='servicio-list'),
    path('crear/', ServicioCreateView.as_view(), name='servicio-create'),
    path('editar/<int:pk>/', ServicioUpdateView.as_view(), name='servicio-update'),
    path('eliminar/<int:pk>/', ServicioDeleteView.as_view(), name='servicio-delete'),
    path('proximos/', ServicioProximosView.as_view(), name='servicio-proximos'),
    path('servicio/pago/<int:pk>/', views.servicio_pago, name='servicio-pago'),
]



