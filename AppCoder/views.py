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
        form= ArticuloFormulario(request.POST)

        if form.is_valid():
            nombre=form.cleaned_data["nombre"]
            cantidad=form.cleaned_data["cantidad"]
            articulo=Articulo() 
            articulo.nombre=nombre 
            articulo.cantidad=cantidad
            articulo.save() 
            form=ArticuloFormulario() 
           
        
       
    else:
        form=ArticuloFormulario() 

    articulos=Articulo.objects.all() 
    context={"articulos":articulos,"form":form} 

    return render (request,"Appcoder/articulos.html",context)

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
           
        
       
    else:
        form=ClienteFormulario() 

    clientes=Cliente.objects.all() 
    context={"clientes":clientes,"form":form} 

    return render (request,"Appcoder/clientes.html",context)

def carrito (request):
    if request.method=="POST":
        form=CarritoFormulario(request.POST)

        if form.is_valid():
            nombre=form.cleaned_data["nombre"]
            cantidad=form.cleaned_data["cantidad"]
            carrito=Carrito()
            carrito.nombre=nombre
            carrito.cantidad=cantidad
            carrito.save()
            form=CarritoFormulario()
            
        else:
            pass

    else:
        form=CarritoFormulario()
        carritos=Carrito.objects.all()
        context={"articulos":carritos, "form":form}
        return render (request,"AppCoder/carrito.html",context)


def buscarArticulo(request):
    return render(request, "AppCoder/busquedaArticulos.html")

def buscandoArticulo(request):
    articuloIngresado= request.GET["nombre"]
    if articuloIngresado!="":
        articulos=Articulo.objects.filter(nombre__icontains=articuloIngresado) #nombre==articuloIngresado
        print(articulos)
        return render(request, "AppCoder/resultadosBusquedaArticulos.html", {"articulos": articulos})
    else:
        return render(request, "AppCoder/busquedaArticulos.html", {"mensaje": "No se ingreso el nombre del artículo"})