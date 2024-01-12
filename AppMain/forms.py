from django import forms
from .models import Categoria

class ClienteForm(forms.Form):
    nombre_completo = forms.CharField(label="Nombre Completo", max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fecha_nacimiento = forms.DateField(label="Fecha de Nacimiento", widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    dni = forms.CharField(label="DNI", max_length=8, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))

class CategoriaForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    descripcion = forms.CharField(label="Descripción", widget=forms.Textarea(attrs={'class': 'form-control'}))

class ProductoForm(forms.Form):
    CATEGORIA_CHOICES = [(x.id, x.nombre) for x in Categoria.objects.all()]
    nombre = forms.CharField(label="Nombre", max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    descripcion = forms.CharField(label="Descripción", widget=forms.Textarea(attrs={'class': 'form-control'}))
    categoria = forms.ChoiceField(label="Categoría", choices=CATEGORIA_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    stock = forms.IntegerField(label="Stock", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    precio = forms.DecimalField(label="Precio", max_digits=8, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    activo = forms.BooleanField(label="Activo", widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))