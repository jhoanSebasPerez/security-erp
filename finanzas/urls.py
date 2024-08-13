from django.urls import path
from .views import reporte_financiero

urlpatterns = [
    path('reporte/', reporte_financiero, name='reporte_financiero'),
]