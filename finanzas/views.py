from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def reporte_financiero(request):
    # Esta es una vista de ejemplo que podría estar sujeta a permisos
    return Response({"mensaje": "Acceso al reporte financiero concedido"})