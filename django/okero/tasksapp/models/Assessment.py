# -*- coding: utf-8 -*-
"""Clase que representa un  valoracion"""


from django.db import models


class Assessment(models.Model):
    """  EL tipo es sobre lo que se esta valorando, no el que valora es decir una valoracion de un contratador sobre un
    trabajador sera de tipo WORKER """

    CONTRACTOR = 1
    WORKER = 2
    TYPES = (
        (CONTRACTOR, 'Contratante'),
        (WORKER, 'Trabajador'),
    )
    message = models.TextField()
    note = models.IntegerField(choices=[(i, str(i)) for i in range(6)])
    date = models.DateTimeField(auto_now=True)
    task = models.ForeignKey('tasksapp.Task', on_delete=models.SET_NULL, null=True, blank=True)
    type = models.IntegerField(choices=TYPES)
