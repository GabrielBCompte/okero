# -*- coding: utf-8 -*-
"""Clase que representa un usuario personalizado para tener más funcionalidades
de los que proporciona el usuario estándar de Django.
"""


from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _


class Booper(AbstractUser):
    """Añadimos el campo phone number que guarda el número de telefono, el phone regex es una expresion regular para 
    verificar que el número tiene un formato correcto"""
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message=_("El formato del número de teléfono es incorrecto"))
    username = models.CharField(validators=[phone_regex], max_length=17, blank=True, unique=True)
    banned = models.BooleanField(default=False)
    description = models.TextField()
    categories = models.ManyToManyField('tasksapp.Category')
    #TODO: Implementar fotografia de perfil
    favorite_tasks = models.ManyToManyField(to='tasksapp.Task')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(blank=True, null=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now=True)
