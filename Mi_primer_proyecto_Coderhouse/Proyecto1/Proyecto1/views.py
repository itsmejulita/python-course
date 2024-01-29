from django.template import Template, Context 
from django.http import HttpResponse
from datetime import datetime 

def saludo(request):
    return HttpResponse("Hola Juliana Fenoglio, como te va?")

def hoy(request): 
    fecha = datetime.now()

    return HttpResponse(f"El día de hoy es {fecha}.")

def prueba (request): 
    
    miHtml = open("C:/Users/Acer.Acer-PC/Documents/python course/Mi_primer_proyecto_Coderhouse/Proyecto1/Proyecto1/Plantillas/plantilla1.html")

    plantilla = Template(miHtml.read())

    miHtml.close()

    micontexto = Context()

    documento = plantilla.render(micontexto)

    return HttpResponse(documento)