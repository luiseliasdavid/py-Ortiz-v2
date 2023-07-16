from django.shortcuts import get_object_or_404
from django.http import HttpResponse

#from .models import User
User = {
    id:1
}

def user_detail(request, user_id):
    try:
        user = get_object_or_404(User, id=user_id)
        # Realiza otras operaciones con el objeto "user" si existe
        return HttpResponse(f"Detalles del usuario: {user.username}")
    except User.DoesNotExist:
        return HttpResponse("El usuario no existe.", status=404)
