# M7-L6-Django-CRUD
proyecto educativo de implementacion de CRUDusando vistas y ORM de Django


# Actividad M7-L6: Implementación de Operaciones CRUD con Django

## Descripción

En esta actividad se desarrolló una aplicación Django que implementa las operaciones básicas de un CRUD (Create, Read, Update y Delete) sobre un modelo llamado `Libro`. Para ello se utilizaron vistas, el ORM de Django, plantillas HTML y rutas dinámicas.

## Funcionalidades implementadas

- Crear un nuevo libro.
- Listar todos los libros registrados.
- Editar la información de un libro existente.
- Eliminar un libro previa confirmación.
- Navegación entre las distintas vistas mediante URLs de Django.
- Protección de formularios utilizando `{% csrf_token %}`.

## Estructura principal

- `models.py`: define el modelo `Libro`.
- `views.py`: contiene las vistas CRUD.
- `urls.py`: configura las rutas de acceso a cada operación.
- `templates/`: incluye las plantillas HTML utilizadas por la aplicación.

## ¿Cómo funciona el flujo completo de una operación CRUD?

El flujo comienza cuando el usuario accede a una URL específica, por ejemplo `/libros/crear/`. Django dirige la solicitud a la vista correspondiente definida en `views.py`. Si el usuario envía un formulario, la vista procesa los datos mediante el ORM y realiza la operación solicitada sobre la base de datos (crear, consultar, actualizar o eliminar registros). Finalmente, la vista devuelve una respuesta renderizando una plantilla HTML o redireccionando al listado de libros.

En resumen:

1. El usuario accede a una URL.
2. Django dirige la petición a una vista.
3. La vista interactúa con el modelo mediante el ORM.
4. Se ejecuta la operación en la base de datos.
5. Se muestra una plantilla HTML con el resultado o se redirecciona a otra vista.

## ¿Qué aprendí sobre el enrutamiento y los parámetros dinámicos en URLs?

Aprendí que el sistema de enrutamiento de Django permite asociar una URL con una función específica en `views.py`. Además, los parámetros dinámicos, como `<int:id>`, permiten capturar valores desde la URL para identificar un registro concreto de la base de datos.

Por ejemplo:

```python
path("editar/<int:id>/", views.editar_libro, name="editar_libro")
```

En este caso, el valor `id` corresponde al identificador del libro que será editado o eliminado, facilitando el acceso a registros específicos sin necesidad de crear una ruta distinta para cada uno.

## Conclusión

Esta actividad permitió comprender cómo Django integra modelos, vistas, plantillas y URLs para implementar un CRUD completo utilizando el ORM, simplificando el acceso a la base de datos y favoreciendo un desarrollo organizado y seguro.