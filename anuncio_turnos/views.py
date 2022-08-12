from django.http import HttpResponse
from django.template import loader
from admin_turnos.models import Anuncios
from django.views import View
from django.http import JsonResponse

def caller(request):
  template = loader.get_template('anuncio_turnos/caller.html')
  
  return HttpResponse(template.render({}, request))


class callerws(View):
    def get(self, request):

        items = Anuncios.objects.all()[:15]

        tabla = '<table class = "table table-striped text-uppercase" style = "width: 85%;">'
        i = 0
        for item in items:
            tabla = tabla + '<tr>'
            if i==0:
              tabla = tabla + '<td class = "text-center" style = "width: 30%; background-color: aquamarine;font-size: 90px;font-weight: bold;">'+ item.decorador.upper() + str(item.contador) +'</td><td style="width: 30%; background-color: aquamarine;font-size: 90px;font-weight: bold;">'+item.lugar.upper()+'</td>'
            else:
              tabla = tabla + '<td class = "text-center" style = "width: 30%; background-color: beige;font-size: 50px;font-weight: bold;">'+ item.decorador.upper() + str(item.contador) +' </td><td style = "width: 30%; background-color: beige;font-size: 50px;font-weight: bold;" >'+item.lugar.upper()+'</td>'

            tabla = tabla + '</tr>'
            i += 1
        
        tabla = tabla+'</table>'
        data = {'table': tabla}
        return JsonResponse(data, status=201)

