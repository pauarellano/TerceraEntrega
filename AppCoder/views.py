from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from .forms import *

# Create your views here.

def crear_cliente(request):
    usuario=Cliente (email="pau.arellano@outlook.es",contrasena="123456")
    usuario.save()
    creacionExitosa=f"El usuario {usuario.email} ha sido creado exitosamente"

    return HttpResponse(creacionExitosa)

def inicio(request):
    return render(request,'AppCoder/inicio.html')

def articulos (request):
    if request.method=="POST":
        form=ArticuloFormulario(request.POST)

        if form.is_valid():
            nombre=form.cleaned_data["nombre"]
            cantidad=form.cleaned_data["cantidad"]
            articulo=Articulo()
            articulo.nombre=nombre
            articulo.cantidad=cantidad
            articulo.save()
            form=ArticuloFormulario()
            return render (request,"AppCoder/articulos.html")
    else:
        form=ArticuloFormulario()
        articulos=Articulo.objects.all
        context={"articulos":articulos, "form":form}
        return render (request,"AppCoder/articulos.html",context)

def clientes (request):

    if request.method=="POST":
        form= ClienteFormulario(request.POST)

        if form.is_valid():
            nombre=form.cleaned_data["nombre"]
            apellido=form.cleaned_data["apellido"]
            email=form.cleaned_data["email"]
            contrasena=form.cleaned_data["contrasena"]
            cliente=Cliente() 
            cliente.nombre=nombre 
            cliente.apellido=apellido
            cliente.email=email
            cliente.contrasena=contrasena
            cliente.save() 
            form=ClienteFormulario() 
            return render (request,"AppCoder/clientes.html")
        
       
    else:
        form=ClienteFormulario() 

    clientes=Cliente.objects.all 
    context={"clientes":clientes,"form":form} 

    return render (request,"Appcoder/clientes.html",context)

def carrito (request):
    if request.method=="POST":
        form=CarritoFormulario(request.POST)

        if form.is_valid():
            nombre=form.cleaned_data["nombre"]
            cantidad=form.cleaned_data["cantidad"]
            carrito1=Carrito()
            carrito1.nombre=nombre
            carrito1.cantidad=cantidad
            carrito1.save()
            form=CarritoFormulario()
            return render (request,"AppCoder/carrito.html")
    else:

        form=CarritoFormulario()

    carrito1=Carrito.objects.all
    context={"carritos":carrito1, "form":form}
    return render (request,"AppCoder/carrito.html",context)