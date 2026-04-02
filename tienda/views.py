from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.urls import reverse

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
    """Vista de inicio de sesión usando AuthenticationForm de Django."""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # form.get_user() devuelve el usuario validado por el formulario
            login(request, form.get_user())
            message = f'Bienvenido, {form.get_user().username}. ¡Buena sesión!'
            messages.success(request, message)
            url = reverse('tienda:index')
            return redirect(url)
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    else:
        form = AuthenticationForm(request)

    template = 'tienda/pages/login.html'
    context = {'form': form}
    return render(request, template, context)


def register(request):
    """Vista de registro de nuevo usuario."""
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            message = f'Usuario {user.username} registrado correctamente. Ya puedes iniciar sesión.'
            messages.success(request, message)
            url = reverse('tienda:login')
            return redirect(url)
        else:
            messages.error(request, 'Por favor corrige los errores del formulario.')
    else:
        form = RegisterForm()

    template = 'tienda/pages/register.html'
    context = {'form': form}
    return render(request, template, context)

@login_required
def logout_view(request):
    """Cierra la sesión del usuario autenticado."""
    logout(request)
    messages.success(request, 'Has cerrado sesión correctamente.')
    url = reverse('tienda:login')
    return redirect(url)


@login_required
def panel(request):
    """Panel del usuario — vista protegida, solo para usuarios autenticados."""
    template = 'tienda/pages/panel.html'
    context = {'user': request.user}
    return render(request, template, context)


@login_required
def productos_admin(request):
    """Gestión de productos — vista protegida, solo visualización."""
    template = 'tienda/pages/productos_admin.html'
    context = {'productos': PRODUCTOS}
    return render(request, template, context)
