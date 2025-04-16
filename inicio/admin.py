from django.contrib import admin
from .models import Articulos


class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('articulo', 'marca', 'modelo','caracteristicas')
    search_fields = ('articulo', 'marca', 'modelo','caracteristicas')
    date_hierarchy = 'created'
    list_filter = ('articulo', 'marca', 'modelo','caracteristicas')

# Register your models here.
admin.site.register(Articulos, AdministrarModelo)
