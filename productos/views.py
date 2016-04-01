from django.shortcuts import render

def producto_list(request):
    return render(request, 'productos/producto_list.html', {})
