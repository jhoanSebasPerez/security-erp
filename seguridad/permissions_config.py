url_permission_map = {
    '/api/finanzas/reporte/': 'read_finance',
    '/api/finanzas/agregar-reporte': 'write_finance',
}

url_allowed = [
    '/api/token/',
    '/api/token/refresh/',
    '/api/schema/',
    '/api/schema/swagger-ui/',
    '/api/schema/redoc/',
]