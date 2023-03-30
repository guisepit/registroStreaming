from django.contrib import admin
from .models import Servicio

# Register your models here.
@admin.register(Servicio)
class Servicio(admin.ModelAdmin):
    list_display=('nombre', 'plataforma', 'fecha_suscripcion', 'monto_pagado', 'proxima_fecha_vencimiento')