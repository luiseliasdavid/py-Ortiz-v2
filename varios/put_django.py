from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views import View
from .models import MiModelo

class ActualizarObjetoView(View):
    def put(self, request, pk):
        # Obtener el objeto existente que queremos actualizar
        objeto = get_object_or_404(MiModelo, pk=pk)

        # Realizar la actualización con los datos proporcionados en el cuerpo de la solicitud PUT
        # Por ejemplo, si el cuerpo contiene un campo "nombre", actualizaremos el nombre del objeto.
        objeto.nombre = request.PUT.get('nombre', objeto.nombre)
        objeto.save()

        # Devolver una respuesta JSON con la información actualizada
        return JsonResponse({'mensaje': 'Objeto actualizado exitosamente.'})
