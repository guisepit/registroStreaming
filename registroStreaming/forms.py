from django import forms
from .models import Servicio

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ('nombre', 'plataforma', 'fecha_suscripcion', 'monto_pagado', 'proxima_fecha_vencimiento')
        widgets = {
        'fecha_suscripcion': forms.DateInput(attrs={'type': 'date'}),
        'proxima_fecha_vencimiento': forms.DateInput(attrs={'type': 'date'}),
        }