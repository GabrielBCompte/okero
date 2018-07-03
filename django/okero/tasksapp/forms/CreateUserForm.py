# -*- coding: utf-8 -*-
from django import forms
from tasksapp.models import Booper


class CreateUserForm(forms.ModelForm):
    """Formulario para crear usuarios. Excluimos los campos is_staff(inutil), is_active(un script se encargara de
    medirlo en el futuro) y date_joined (se genera en datetime.now)
    """

    class Meta:
        model = Booper
        exclude = ['is_staff', 'is_active', 'date_joined']
