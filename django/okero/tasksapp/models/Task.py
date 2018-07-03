# -*- coding: utf-8 -*-
"""Clase que representa un  tarea"""


from django.db import models
from okero.settings import CURRENCY_TYPES

class Task(models.Model):
    OPEN = 1
    TAKEN = 2
    CLOSE = 3
    STATES = (
        (OPEN, 'Open'),
        (TAKEN, 'Taken'),
        (CLOSE, 'Close'),
    )

    title = models.CharField(max_length=90, blank=True)
    description = models.TextField()
    contractor = models.ForeignKey('tasksapp.Booper', on_delete=models.CASCADE, related_name='offers')
    worker = models.ForeignKey('tasksapp.Booper', null=True, blank=True, on_delete=models.SET_NULL, related_name='works')
    category = models.ManyToManyField('tasksapp.Category')
    state = models.IntegerField(choices=STATES)
    #  TODO: Implementar fotografias
    reward = models.IntegerField()
    currency = models.IntegerField(choices=CURRENCY_TYPES)
    date = models.DateTimeField(auto_now=True)