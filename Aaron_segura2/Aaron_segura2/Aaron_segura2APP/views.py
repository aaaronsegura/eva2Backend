from django.shortcuts import redirect, render

#from Aaron_segura2.models import Formulario
#from Aaron_segura2


# Create your views here.
def index(request):
    return render(request,'index.html')

"""def listarPersona(request):
    Persona = persona.objects.all()
    data = {'perso':Persona}
    return render(request,'ListarPersonas.html',data)


def agregarPersona(request):
    form = FormsPersona()

    if request.method == 'POST':
        form = FormsPersona(request.POST)
        if form.is_valid() :
            form.save()
        return index(request)

    data ={'formP':form}
    return render(request,'agregarPersona.html',data)


def eliminarPersona(request,id):
    Perso = persona.objects.get(id=id)
    Perso.delete()
    return redirect('/listarP/')

def ActualizarPersona(request,id):
    Perso = persona.objects.get(id=id)
    form = FormsPersona(instance=Perso)
    if request.method == 'POST':
        form = FormsPersona(request.POST,instance=Perso)
        if form.is_valid():
            form.save()
        return index(request)    

        

    data = {'form':form}
    return render(request,'agregarPersona.html',data)
    """