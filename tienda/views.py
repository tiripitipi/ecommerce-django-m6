from django.shortcuts import render

# Catálogo de productos — los mismos del Rincón del Tenis desde el módulo 2
PRODUCTOS = [
    {'id': 1, 'nombre': 'Raqueta Wilson Pro Staff',        'categoria': 'Raquetas',   'precio': 89990},
    {'id': 2, 'nombre': 'Zapatillas Asics Gel-Dedicate 8', 'categoria': 'Calzado',    'precio': 49990},
    {'id': 3, 'nombre': 'Pelotas Babolat x4',              'categoria': 'Pelotas',    'precio': 8990},
    {'id': 4, 'nombre': 'Overgrip Wilson Pro x3',          'categoria': 'Accesorios', 'precio': 4990},
    {'id': 5, 'nombre': 'Camiseta Torino Verde Ellesse',   'categoria': 'Ropa',       'precio': 19990},
    {'id': 6, 'nombre': 'Antivibrador Head Xtra Damp x2',  'categoria': 'Accesorios', 'precio': 8990},
]


def index(request):
    """Vista principal — muestra el catálogo al público."""
    template = 'tienda/pages/index.html'
    context = {'productos': PRODUCTOS}
    return render(request, template, context)


def login_view(request):
    pass


def register(request):
    pass


def logout_view(request):
    pass


def panel(request):
    pass


def productos_admin(request):
    pass
