from .models import Equipo

def total_equipos(request):
    return {
        'total_equipos': Equipo.objects.count()
    }