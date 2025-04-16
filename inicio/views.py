
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArticulosForm
from .models import Articulos
from django.contrib import messages
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from django.template.loader import get_template
from xhtml2pdf import pisa
from reportlab.pdfgen import canvas
from django.contrib.auth.decorators import login_required
#VISTA DEL MENU PRINCIPAL
@login_required
def principal(request):
    return render(request, 'almacen/inicio.html')

@login_required #el usuario necesita estar loguado para acceder 
def altaArticulos(request):
    return render(request, 'almacen/altaArticulo.html')
@login_required
def almacen(request):
    resguardante_seleccionado = request.GET.get("resguardante", "")
    
    if resguardante_seleccionado:
        articulos = Articulos.objects.filter(resguardante=resguardante_seleccionado)
    else:
        articulos = Articulos.objects.all()

    resguardantes = Articulos.objects.values_list("resguardante", flat=True).distinct()
    
    return render(request, "almacen/almacen.html", {
        "AT": articulos,
        "resguardantes": resguardantes,
        "resguardante_seleccionado": resguardante_seleccionado
    })

#VISTA PARA EL ALTA DE UN ARTICULO
def alta(request):
    if request.method == 'POST':
        form = ArticulosForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'El artículo se ha registrado exitosamente.')

            return redirect( 'almacen')
    else:
        form = ArticulosForm()
    return render(request, 'almacen/altaArticulo.html', {'form': form})

def eliminar(request, articulo_id):
    articulo = get_object_or_404(Articulos, id=articulo_id)
    if request.method == 'POST':
        articulo.delete()
        return redirect('almacen')
    return render(request, 'almacen/eliminar.html', {'articulo': articulo})

def editar(request, articulo_id):
    articulo = get_object_or_404(Articulos, id=articulo_id)
    if request.method == 'POST':
        form = ArticulosForm(request.POST, instance=articulo)
        if form.is_valid():
            form.save()
            return redirect('almacen')
    else:
        form = ArticulosForm(instance=articulo)
    return render(request, 'almacen/editar.html', {'form': form, 'articulo': articulo})


def generar_pdf(request):
    resguardante = request.GET.get('resguardante')

    if resguardante:
        articulos = Articulos.objects.filter(resguardante=resguardante)
    else:
        articulos = Articulos.objects.all()
        
    template = get_template('almacen/pdf.html')
    html = template.render({'articulos': articulos, 'resguardante': resguardante})

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte.pdf"'
    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('Error al generar PDF')
    return response
     
     