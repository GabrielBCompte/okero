# -*- coding: utf-8 -*-
"""Clase que representa un  denuncia"""


from django.db import models


class Complaint(models.Model):
    title = models.CharField(max_length=90, blank=True)
    message = models.TextField()
    date = models.DateTimeField(auto_now=True)
    receiver = models.ForeignKey('tasksapp.Booper', on_delete=models.CASCADE, related_name='complaints_received')
    writer = models.ForeignKey('tasksapp.Booper', on_delete=models.CASCADE, related_name='complaints_wrote')