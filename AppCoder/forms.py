from django import forms

class ClienteFormulario(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    email=forms.EmailField()
    contrasena=forms.CharField(max_length=20)

class CarritoFormulario(forms.Form):
    nombre=forms.CharField(max_length=50)
    cantidad=forms.IntegerField()    

class ArticuloFormulario(forms.Form):
    nombre=forms.CharField(max_length=50)
    cantidad=forms.IntegerField()