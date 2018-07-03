# -*- coding: utf-8 -*-
"""Clase que representa un  notificacion"""


from django.db import models
from okero.settings import CURRENCY_TYPES


class Appeal(models.Model):
    ACCEPTED = 1
    REJECTED = 2
    PENDENT = 3
    APPEAL_STATUS = (
        (ACCEPTED, 'Aceptada'),
        (REJECTED, 'Rechazada'),
        (PENDENT, 'Pendiente'),
    )
    task = models.ForeignKey('tasksapp.Task', on_delete=models.SET_NULL, null=True, blank=True)
    worker = models.ForeignKey('tasksapp.Booper', on_delete=models.CASCADE)
    reward = models.IntegerField()
    currency = models.IntegerField(choices=CURRENCY_TYPES)
    date = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=APPEAL_STATUS, default=PENDENT)


