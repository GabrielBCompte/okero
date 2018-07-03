# -*- coding: utf-8 -*-
"""Clase que representa un  categoria"""


from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=90, blank=True)
    description = models.TextField()
