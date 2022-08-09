from asyncio.windows_events import NULL
from datetime import date, datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth import login, logout, authenticate
from admin_turnos.forms import CustomLoginForm, CustomUserCreationForm, CustomTramitesForm, CustomUserUpdateForm, CustomClientesForm, RecCustomClientesForm, FinderApellido
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from admin_turnos.models import Anuncios, Ingresos, Tramites, Clientes, Contadores
from django.contrib.auth.decorators import login_required
from django.conf import settings


def main(request):
    show = "false"
    datos_cont=Contadores.objects.all()

    if datos_cont.count()==0: 
        cont = Contadores(descripcion="INGRESOS",tipo="INGR",valor="0",fec_ult_actual=date.today())
        cont.save()
        

    template = loader.get_template('admin_turnos/index.html')
    context = {
      'show': show
    }
    return HttpResponse(template.render(context, request))


def about(request):
    show = "false"

    template = loader.get_template('admin_turnos/about.html')
    context = {
        'show': show
    }
    return HttpResponse(template.render(context, request))


def sessionin(request):
    show = "false"

    if request.method == "POST":
        form = CustomLoginForm(request, data=request.POST)

        if form.is_valid:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                return redirect('main')
            else:
                return render(request, "admin_turnos/login.html", {"mensaje": "Datos incorrectos",
                                                                   "form": form,
                                                                   "show": show})
        else:
            return render(request, "admin_turnos/login.html", {"mensaje": "Datos inválidos",
                                                               "form": form,
                                                               "show": show})

    form = CustomLoginForm()

    return render(request, "admin_turnos/login.html", {"form": form,
                                                       "show": show})



@login_required
def resetcontadores(request):
    Contadores.objects.update(valor=0)

    return redirect('resetlist')

@login_required
def sesionout(request):
    logout(request)
    return redirect('main')


class ProfileView(UpdateView):
    model = User
    success_url = reverse_lazy('main')
    form_class = CustomUserUpdateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show'] = "false"
        return context

class UserUpdateView(UpdateView):
    model = User
    success_url = reverse_lazy('ulist')
    form_class = CustomUserUpdateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show'] = "false"
        return context

class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('ulist')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show'] = "false"
        return context

class UserCreateView(CreateView):
    template_name = 'auth/user_create.html'
    success_url = reverse_lazy('sessionin')
    form_class = CustomUserCreationForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show'] = "false"
        return context

class UserListView(ListView):
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show'] = "false"
        return context

class UserDetailView(DetailView):
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show'] = "false"
        return context

class TramitesListView(ListView):
    model = Tramites
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show'] = "false"
        return context

class TramitesDetailView(DetailView):
    model = Tramites

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show'] = "false"
        return context

class TramitesCreateView(CreateView):
    template_name = 'admin_turnos/tramites_create.html'
    success_url = reverse_lazy('tlist')
    form_class = CustomTramitesForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show'] = "false"
        return context

class TramitesUpdateView(UpdateView):
    model = Tramites
    success_url = reverse_lazy('tlist')
    form_class = CustomTramitesForm
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show'] = "false"
        return context


class TramitesDeleteView(DeleteView):
    model = Tramites
    success_url = reverse_lazy('tlist')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show'] = "false"
        return context


class ClientesListView(ListView):
    model = Clientes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show'] = "false"
        context['media'] = settings.MEDIA_URL
        return context


class ClientesDetailView(DetailView):
    model = Clientes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show'] = "false"
        context['media'] = settings.MEDIA_URL
        return context

class ClientesCreateView(CreateView):
    template_name = 'admin_turnos/clientes_form.html'
    success_url = reverse_lazy('clist')
    form_class = CustomClientesForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show'] = "false"
        context['titulo'] = 'Alta de Cliente'
        return context

class ClientesUpdateView(UpdateView):
    model = Clientes
    success_url = reverse_lazy('clist')
    form_class = CustomClientesForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show'] = "false"
        context['media'] = settings.MEDIA_URL
        context['titulo'] = 'Modificar Cliente'
        return context


class ClientesDeleteView(DeleteView):
    model = Clientes
    success_url = reverse_lazy('clist')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show'] = "false"
        return context

class ContadoresListView(ListView):
    model = Contadores

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show'] = "false"
        return context


class IngresosListView(ListView):   
    model = Ingresos

    def get_queryset(self):
        return Ingresos.objects.order_by('recibido').values()
        #esto es para poder traer todos los que hayan pasado por recepcion [S/N]: ordena por recibido ASC

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show'] = "false"
        context['media'] = settings.MEDIA_URL
        return context


class AnunciosListView(ListView):
    model = Anuncios

    def get_queryset(self):
        return Anuncios.objects.all()
        #trae todos los anuncios ordenardos por Fecha de Anuncio Desc

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show'] = "false"
        context['media'] = settings.MEDIA_URL
        return context


@login_required
def recdetail(request,ning):
    ingreso = Ingresos.objects.filter(id=ning)
    cliente = Clientes.objects.filter(documento=ingreso[0].documento)

    apenom = NULL

    if cliente:
        Ingresos.objects.filter(id=ning).update(id_cliente=cliente[0].id)
        apenom=cliente[0].apellido+' '+cliente[0].nombres

    show = "false"
    return render(request, "admin_turnos/ingresos_detail.html", {"show": show, 'ingreso':ingreso[0], 'apenom':apenom})


@login_required
def Lugardetail(request, ning):
    ingreso = Ingresos.objects.filter(id=ning)
    cliente = Clientes.objects.filter(documento=ingreso[0].documento)

    apenom = NULL
    fec_nac = NULL
    picture = NULL
    if cliente:
        apenom = cliente[0].apellido+' '+cliente[0].nombres
        fec_nac = cliente[0].fec_nac
        picture = cliente[0].picture

    show = "false"
    return render(request, "admin_turnos/lugares_detail.html", {"show": show, 'ingreso': ingreso[0], 'apenom': apenom, 'fec_nac': fec_nac, 'picture': picture, 'media': settings.MEDIA_URL})


@login_required
def GenerarAnuncio(request,rec,ning,deco,cont):
    #se cambia el valor a RECEPCIONADO = SI
    if  rec == "N":
        Ingresos.objects.filter(id=ning).update(recibido="S")
    anun = Anuncios(id_ingreso=ning, fec_anuncio=datetime.today(), decorador=deco, contador=cont, lugar="RECEPCION")
    anun.save()
    return redirect('recepcion')


@login_required
def LugarGenAnuncio(request, ning, deco, cont, ntram):
    tramite = Tramites.objects.filter(id=ntram)
    anun = Anuncios(id_ingreso=ning, fec_anuncio=datetime.today(),
                    decorador=deco, contador=cont, lugar=tramite[0].lugar)
    anun.save()
    return redirect('lugardetail', ning)

@login_required
def RecClienteCreateView(request,ning,ndoc):
    show = "false"

    if request.method == "POST":
        form = RecCustomClientesForm(request.POST)

        if form.is_valid(): 
            
            cliente = Clientes.objects.filter(documento=ndoc)
            if not cliente:
                form.save()

            return redirect('recdetail',ning=ning)
        else:
            return render(request, "admin_turnos/cliente_recepcion.html", {"mensaje": "Datos inválidos",
                                                            "form": form,
                                                            "show": show,
                                                            "ning":ning})

    form = RecCustomClientesForm()
    form.fields['documento'].initial=ndoc

    return render(request, "admin_turnos/cliente_recepcion.html", {"form": form,
                                                            "show": show,
                                                            "ning":ning})


@login_required
def IngresoAtendido(request, ning):
    Ingresos.objects.filter(id=ning).update(atendido="S",recibido="S")
    return redirect('recepcion')


@login_required
def TurnoFinalAtendido(request, ning):
    Ingresos.objects.filter(id=ning).update(atendido="S", recibido="S")
    return redirect('lugares')


@login_required
def LugarAtendido(request, ning):
    Ingresos.objects.filter(id=ning).update(atendido="-", recibido="S")
    return redirect('lugares')

@login_required
def EliminarAnuncio(request, nanun):
    Anuncios.objects.filter(id=nanun).delete()
    return redirect('anuncios')


@login_required
def IngresoRefresh(request, ning):
    Ingresos.objects.filter(id=ning).update(atendido="N")
    return redirect('recepcion')


@login_required
def LugarRefresh(request, ning):
    Ingresos.objects.filter(id=ning).update(atendido="N")
    return redirect('lugares')

@login_required
def ConfirmarCambioDoc(request,ndoc, ning):
    Ingresos.objects.filter(id=ning).update(documento=ndoc)
    return redirect('recepcion')


@login_required
def ClieIngFin(request, ning):
    show = "false"

    if request.method == "POST":
        form = FinderApellido(request.POST)
        
        sname = request.POST['apellido']
        findclie = Clientes.objects.filter(apellido__contains=sname)
        
        return render(request, "admin_turnos/cliente_ing_finder.html", {"form": form,
                                                                           "show": show,
                                                                           "ning": ning,
                                                                           "findclie": findclie})

    form = FinderApellido()
    
    return render(request, "admin_turnos/cliente_ing_finder.html", {"show": show, "ning": ning, 'form':form})
    

@login_required
def finder(request):
    show = "true"
    tramites = Tramites.objects.filter(activo="S")
    form=NULL
    tramdes=NULL

    if request.method == "POST":
        nbus1 = request.POST['busqueda1']
                
        if nbus1:
            form = Ingresos.objects.filter(id_tramite=nbus1, recibido="S",atendido="N")
            tramdes = Tramites.objects.filter(id=nbus1)
        
            return render(request, "admin_turnos/finder.html", {"show": show, "tramites": tramites, "form":form, "tramdes":tramdes[0].descripcion})
    
    return render(request, "admin_turnos/finder.html", {"show": show, "tramites": tramites, "form": form, "tramdes":"NO SELECCIONADO"})

@login_required
def Lugares(request):
    show = "false"

    #esto es para poder traer todos los que hayan pasado por recepcion [S]: ordena por recibido ASC
    form = Ingresos.objects.filter(recibido="S", atendido="S").order_by('atendido').values() | Ingresos.objects.filter(recibido="S", atendido="N").order_by('atendido').values()
    
    return render(request, "admin_turnos/lugares_list.html", {"form": form,
                                                                "show": show})
