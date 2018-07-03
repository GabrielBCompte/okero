# -*- coding: utf-8 -*-
"""Clase que representa un  notificacion"""


from django.db import models


class Notification(models.Model):
    title = models.CharField(max_length=90, blank=True)
    description = models.TextField()
    read = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now=True)
    receiver = models.ForeignKey('tasksapp.Booper', on_delete=models.CASCADE)