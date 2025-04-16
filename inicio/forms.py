from django import forms
from .models import Articulos
class ArticulosForm(forms.ModelForm):
    class Meta:
        model = Articulos
        fields = ['articulo', 'marca', 'modelo', 'serie', 'caracteristicas', 'estado', 'n_inventario','resguardante','area']



