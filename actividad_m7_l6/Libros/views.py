from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect,get_object_or_404
from .models import Libro

def listar_libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/listar_libros.html', {'libros': libros})

def crear_libro(request):
    if request.method == "POST":
        titulo = request.POST["titulo"]
        autor = request.POST["autor"]
        anio = request.POST["anio"]

        Libro.objects.create(
            titulo=titulo,
            autor=autor,
            anio=anio
        )

        return redirect("listar_libros")

    return render(request, "libros/formulario_libro.html")

def editar_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    if request.method == 'POST':
        libro.titulo = request.POST['titulo']
        libro.autor = request.POST['autor']
        libro.anio = request.POST['anio']
        libro.save()
        return redirect('listar_libros')
    return render(request, 'libros/editar_libro.html', {'libro': libro})


def eliminar_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    if request.method == 'POST':
        libro.delete()
        return redirect('listar_libros')
    return render(request, "libros/confirmar_eliminacion.html", {"libro": libro})

