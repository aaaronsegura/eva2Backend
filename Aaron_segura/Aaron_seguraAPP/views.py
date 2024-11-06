from django.shortcuts import redirect, render 
from Aaron_seguraAPP.models import Django_Seminario
from Aaron_seguraAPP.forms import FormSeminario

# Create your views here.
def index (request):
    return render(request, 'index.html')


def listar_inscripciones(request):
    inscripciones = Django_Seminario.objects.all()
    context = {'inscripciones': inscripciones}
    return render(request, 'listar_inscripciones.html', context)


def agregar_inscripcion(request):
    form = FormSeminario()
    if request.method == 'POST':
        form = FormSeminario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listar/')
    context = {'form': form}
    return render(request, 'agregar_inscripcion.html', context)


def eliminar_inscripcion(request, id):
    inscripcion = Django_Seminario.objects.get(id=id)
    inscripcion.delete()
    return redirect('/listar/')


def actualizar_inscripcion(request, id):
    inscripcion = Django_Seminario.objects.get(id=id)
    form = FormSeminario(instance=inscripcion)
    if request.method == 'POST':
        form = FormSeminario(request.POST, instance=inscripcion)
        if form.is_valid():
            form.save()
            return redirect('/listar/')
    context = {'form': form}
    return render(request, 'actualizar_inscripcion.html', context)
