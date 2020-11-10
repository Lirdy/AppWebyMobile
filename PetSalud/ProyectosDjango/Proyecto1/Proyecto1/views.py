from django.http import HttpResponse
import  datetime
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.template import Template, Context

Template_paht="C:\Users\matias\Desktop\2do semestre 2020\Ramo des.app. web y mobile\EntregaPetSalud1\PetSalud\ProyectosDjango\Proyecto1\Proyecto1\plantillas"

def saludo(request):   #primera vista

#return HttpResponse("Bienvenios a la página de PetSalud:Los mejores alimentos para tus mascotas")

  #documento ="""<html>
  #<body>
  #<h1>
  #Bienvenios a la página de PetSalud:Los mejores alimentos para tus mascota
  #</h1>
  #</body>
  #</html>"""

    doc_externo=open("C:/Users/matias/Desktop/2do semestre 2020/Ramo des.app. web y mobile/EntregaPetSalud1/PetSalud/ProyectosDjango/Proyecto1/Proyecto1/plantillas/miplantilla.html")

    plt=Template(doc_externo.read())

    doc_externo.close()

    ctx=Context()

    documento=plt.render(ctx)

    return HttpResponse(documento)


def dameFecha(request):

    fecha_actual =datetime.datetime.now()

    documento ="""<html>
    <body>
    <h2>
    Fecha y hora actuales %s 
    </h2>
    </body>
    </html>"""% fecha_actual
    return HttpResponse(documento)

def privado(request):


	if not request.user.is_autenticated:
	  return redirect('/admin')

     #doc_externo=open("C:/Users/matias/Desktop/2do semestre 2020/Ramo des.app. web y mobile/EntregaPetSalud1/PetSalud/ProyectosDjango/Proyecto1/Proyecto1/plantillas/miplantilla.html")


  template_file =open(template_paht+"/website.html")

	context=Context({"página ctual":"Autentificado","contenido": "Información para usuario autentificados"})

  template =Template(doc_externo.read())

  doc_externo.close()

  response = HttpResponse(template.render(context))
  return response
