from dataclasses import field
from pyexpat import model
from django import forms
from django.forms import ModelForm, widgets
from .models import *


ROLL = [
    ('Admin', 'Administrador'),
    ('Administrativo', 'Administrativo'),
    ('Arquitecto', 'Arquitecto'),
]

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'UserAcces',

            
        ]
        labels = {
            'UserAcces': 'UserAcces',
            
        }

class PostForm(forms.ModelForm):
    UserAcces = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder':'Usuario','size': '50'}),required=True)
    Nombre = forms.CharField(label="", widget=forms.TextInput(attrs={'rows':1,'placeholder':'Nombre','size': '50'}),required=True)
    ApellidoPaterno = forms.CharField(label="", widget=forms.TextInput(attrs={'rows':1,'placeholder':'Apellido Paterno','size': '50'}),required=True)
    ApellidoMaterno = forms.CharField(label="", widget=forms.TextInput(attrs={'rows':1,'placeholder':'Apellido Materno','size': '50'}),required=True)
    Correo = forms.CharField(label="", widget=forms.TextInput(attrs={'rows':2,'placeholder':'Correo Electronico','size': '50'}),required=True)
    Telefono = forms.CharField(label="", widget=forms.TextInput(attrs={'rows':2,'placeholder':'Telefono','size': '50'}),required=True)
    Pass = forms.CharField(label="", widget=forms.TextInput(attrs={'rows':2,'placeholder':'Password','size': '50'}),required=True)
    Roll = forms.ChoiceField(choices = ROLL)
    #geeks_field = forms.ChoiceField(choices = FAVORITE_COLORS_CHOICES)
    
    class Meta:
        model=Usuario
        fields = [
            'UserAcces',
            'Nombre',
            'ApellidoPaterno',
            'ApellidoMaterno',
            'Correo',
            'Telefono',
            'Pass',
            'Roll',
            
        ]
        
