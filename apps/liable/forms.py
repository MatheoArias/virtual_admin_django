from django import forms
from django.forms import ModelForm
from .models import Liable


class LiableForm(ModelForm):

    class Meta:
        model = Liable
        fields = ['code', 'name', 'lastName', 'email', 'telephone', 'workstation', 'image', 'active', 'position']