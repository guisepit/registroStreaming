from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.generic import ListView
from datetime import timedelta
from django.utils import timezone
from .models import Servicio
from django.views import View
from django.contrib import messages
from datetime import date
from .models import Servicio
from .forms import ServicioForm

class ServicioListView(View):
    def get(self, request, *args, **kwargs):
        servicios = Servicio.objects.all()
        context = {'servicios': servicios}
        return render(request, 'servicios/servicio_list.html', context)

class ServicioCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ServicioForm()
        context = {'form': form}
        return render(request, 'servicios/servicio_form.html', context)

    def post(self, request, *args, **kwargs):
        form = ServicioForm(request.POST)
        if form.is_valid():
            servicio = form.save(commit=False)
            servicio.user = request.user
            servicio.save()
            messages.success(request, 'El servicio ha sido creado exitosamente.')
            return redirect('servicio-list')
        context = {'form': form}
        return render(request, 'servicios/servicio_form.html', context)

class ServicioUpdateView(View):
    def get(self, request, pk, *args, **kwargs):
        servicio = get_object_or_404(Servicio, pk=pk)
        form = ServicioForm(instance=servicio)
        context = {'form': form, 'servicio': servicio}
        return render(request, 'servicios/servicio_form.html', context)

    def post(self, request, pk, *args, **kwargs):
        servicio = get_object_or_404(Servicio, pk=pk)
        form = ServicioForm(request.POST, instance=servicio)
        if form.is_valid():
            servicio = form.save(commit=False)
            servicio.save()
            messages.success(request, 'El servicio ha sido actualizado exitosamente.')
            return redirect('servicio-list')
        context = {'form': form, 'servicio': servicio}
        return render(request, 'servicios/servicio_form.html', context)


class ServicioDeleteView(View):
    def post(self, request, pk, *args, **kwargs):
        servicio = get_object_or_404(Servicio, pk=pk)
        servicio.delete()
        messages.success(request, 'El servicio ha sido eliminado exitosamente.')
        return redirect('servicio-list')

class ServicioProximosView(ListView):
    model = Servicio
    template_name = 'servicios/servicio_proximos.html'
    context_object_name = 'servicios'

    def get_queryset(self):
        # Obtener los servicios que vencen en los próximos 7 días
        servicios_proximos = Servicio.objects.filter(
            proxima_fecha_vencimiento__range=(
                timezone.now(), timezone.now() + timedelta(days=7)
            )
        )
        # Obtener los servicios que ya han vencido
        servicios_vencidos = Servicio.objects.filter(
            proxima_fecha_vencimiento__lt=timezone.now()
        )
        # Unir ambos resultados y devolverlos ordenados por fecha de vencimiento
        queryset = servicios_proximos.union(servicios_vencidos).order_by('proxima_fecha_vencimiento')
        return queryset

@require_POST
def servicio_pago(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk)
    servicio.actualizar_vencimiento()
    servicio.save()
    return redirect('servicio-proximos')