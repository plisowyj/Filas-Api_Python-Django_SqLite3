from django.http import HttpResponse
from django.template import loader
from admin_turnos.models import Anuncios

def caller(request):
  form = Anuncios.objects.all()
  first = form.first()
  template = loader.get_template('anuncio_turnos/caller.html')
  context = {"form":form,"first":first}
  return HttpResponse(template.render(context, request))



