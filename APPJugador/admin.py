from django.contrib import admin
from APPJugador.models import Jugador

class JugadorAdmin(admin.ModelAdmin):
    list_display=['nombre', 'apellido', 'tag', 'edad', 'correo', 'estado']

# Register your models here.
admin.site.register(Jugador, JugadorAdmin)