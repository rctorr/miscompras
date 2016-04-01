from django.shortcuts import render
from django.utils import timezone
from .models import Producto

def producto_list(request):
    productos = Producto.objects.filter(fecha_registro__lte=timezone.now()).order_by('fecha_registro')
    return render(request, 'productos/producto_list.html', {'productos': productos})
