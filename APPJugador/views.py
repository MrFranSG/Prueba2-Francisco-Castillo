from django.shortcuts import render
from APPJugador.models import Jugador
from APPJugador.forms import FormJugador
from django.shortcuts import redirect

def index(request):
    return render(request, 'APPJugador/index.html')


def listado(request):
    jugadores=Jugador.objects.all()
    data ={'jugadores':jugadores}
    return render(request,'APPJugador/ListaJugadores.html', data)

def agregarJugadores(request):
    form = FormJugador()
    if request.method == 'POST':
        form = FormJugador(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data ={'form':form}
    return render(request, 'APPJugador/AgregarJugadores.html',data)

def eliminarJugador(request, id):
    jugador=Jugador.objects.get(id=id)
    jugador.delete()
    return redirect('/ListaJugadores.html')

def actualizarJugador(request,id):
    jugador=Jugador.objects.get(id=id)
    form=FormJugador(instance=jugador)
    if request.method == 'POST':
        form = FormJugador(request.POST, instance=jugador)
        if form.is_valid():
            form.save()
        return index(request)
    data={'form':form}
    return render(request, 'APPJugador/AgregarJugadores.html',data)



# Create your views here.
