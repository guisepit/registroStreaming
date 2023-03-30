

# Create your models here.
from django.db import models
import datetime

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    plataforma = models.CharField(max_length=100)
    fecha_suscripcion = models.DateField()
    monto_pagado = models.DecimalField(max_digits=10, decimal_places=2)
    proxima_fecha_vencimiento = models.DateField()

    def __str__(self):
        return self.nombre

    def actualizar_vencimiento(self):
    # obtenemos la fecha actual
        fecha_actual = datetime.date.today()

    # verificamos si la fecha de vencimiento ya ha pasado
        if fecha_actual > self.proxima_fecha_vencimiento:
            # si ha pasado, actualizamos la fecha de vencimiento al siguiente mes
            proximo_mes = self.proxima_fecha_vencimiento.month + 1
            proximo_ano = self.proxima_fecha_vencimiento.year
            if proximo_mes == 13:
                proximo_mes = 1
                proximo_ano += 1
            self.proxima_fecha_vencimiento = datetime.date(proximo_ano, proximo_mes, self.proxima_fecha_vencimiento.day)
        else:
            # si todavía no ha pasado, simplemente agregamos un mes a la fecha de vencimiento actual
            proximo_mes = self.proxima_fecha_vencimiento.month + 1
            proximo_ano = self.proxima_fecha_vencimiento.year
            if proximo_mes == 13:
                proximo_mes = 1
                proximo_ano += 1
            dia = min(self.proxima_fecha_vencimiento.day, 28)
            self.proxima_fecha_vencimiento = datetime.date(proximo_ano, proximo_mes, dia)

    # guardamos los cambios en la base de datos
        self.save()