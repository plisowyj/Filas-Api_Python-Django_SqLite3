from django.http import HttpResponse
from django.template import loader
from admin_turnos.models import Tramites, Contadores, Ingresos
from datetime import datetime
from django.shortcuts import redirect


def touch(request):
  template = loader.get_template('emision_turnos/touch.html')
  tramites = Tramites.objects.filter(activo="S")[:6]
  context = {'tramites': tramites}
  return HttpResponse(template.render(context, request))


def confirm(request,ndoc,ntram):
  template = loader.get_template('emision_turnos/touch_input.html')

  ndoc = ndoc
  ntram = ntram

  tram_lugar = Tramites.objects.filter(id=ntram)
  decora = tram_lugar[0].decorador
  descripcion = tram_lugar[0].descripcion

  validar_ing = Ingresos.objects.filter(id_tramite=ntram).filter(documento=ndoc).filter(recibido="N").filter(atendido="N")
  if not validar_ing :
    cont = Contadores.objects.filter(tipo="INGR")
    numera = cont[0].valor + 1
    Contadores.objects.filter(tipo="INGR").update(valor=numera)

    ingreso = Ingresos(id_tramite=ntram,
                       tram_detalle=descripcion,
                       decorador=decora,
                       contador=numera,
                       id_cliente=0,
                       fec_ingreso=datetime.today(),
                       recibido="N",
                       atendido="N",
                       documento=ndoc)
    ingreso.save()

    context = {'ndoc':ndoc,
              'sdesc': descripcion,
              'turno': decora + str(numera)}
    return HttpResponse(template.render(context, request))
  else:
    return redirect('touch')
