from django.shortcuts import render
from urllib.parse import urlparse, parse_qs

def capturar_utm(request):
    utm_source = request.GET.get('utm_source')
    utm_medium = request.GET.get('utm_medium')
    utm_campaign = request.GET.get('utm_campaign')

    # Puedes realizar cualquier acción con los valores de los UTM tags aquí
    # Por ejemplo, guardarlos en una base de datos, realizar análisis, etc.

    return render(request, 'tu_template.html', {
        'utm_source': utm_source,
        'utm_medium': utm_medium,
        'utm_campaign': utm_campaign,
    })
