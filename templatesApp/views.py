
from contextlib import _RedirectStream, redirect_stderr, redirect_stdout
from django.shortcuts import render
from templatesApp.forms import FormularioUsuario
from templatesApp.models import User   
from django.http import HttpRequest
from django.shortcuts import redirect
# Create your views here.


def empleado(request):  
    return render(request, "templatesApp/index.html")


def ListEmpleados(request):
    user = User.objects.all()
    data = {'user' : user}
    return render(request, 'templatesApp/empleados.html', data)   


def prosesarFormulario(request):
    form = FormularioUsuario()
    if request.method == 'POST':
        form = FormularioUsuario(request.POST)
        if form.is_valid():
          form.save()
        return empleado(request)
    data = {'form' : form}        
    return render(request, "templatesApp/usuarios.html", data)


def eliminar(request, id):
    user = User.objects.get(id = id)
    user.delete()
    return redirect('../usuarios')



def actualizar(request, id):
    user = User.objects.get(id = id)
    form = FormularioUsuario(instance=user)
    if request.method == 'POST':
        form = FormularioUsuario(request.POST, instance=user)
        if form.is_valid():
          form.save()
        return empleado(request)
    data = {'form' : form}        
    return render(request, "templatesApp/usuarios.html", data)