from django.shortcuts import render, redirect
from .models import Libro
from .forms import LibroForm

def inicio(request):
    return render(request, 'paginas/inicio.html', {})

def nosotros(request):
    return render(request, 'paginas/nosotros.html', {})

def libros(request):
    libros = Libro.objects.all()
    context = {
        'libros': libros
    }
    return render(request, 'Libros/libros.html', context)

def crear_libro(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    context = {
        'formulario': formulario
    }
    return render(request, 'Libros/crear.html', context)

def editar_libro(request, id):
    libro = Libro.objects.get(id=id)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('libros')
    context = {
        'formulario': formulario
    }
    return render(request, 'Libros/editar.html', context)

def eliminar_libro(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('libros')