from django.shortcuts import render


def index(request):
    """Vista principal — muestra el catálogo al público."""
    template = 'tienda/pages/index.html'
    context = {}
    return render(request, template, context)
