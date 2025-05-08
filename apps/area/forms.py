from django import forms
from django.forms import ModelForm
from .models import Area

class AreaForm(ModelForm):
    
    class Meta:
        model=Area
        fields=''
        fields=['description']
    
    
    
    
        
    