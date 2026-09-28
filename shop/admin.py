from django.contrib import admin
from shop.models import Pelicula

# Register your models here.

class PeliculaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'director', 'genero', 'anio', 'fecha_estreno', 'disponible']

admin.site.register(Pelicula, PeliculaAdmin)