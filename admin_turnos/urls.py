from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main, name='main'),
    path('about/', views.about, name='about'),
    path('login/', views.sessionin, name='sessionin'),
    path('finder/', views.finder, name='finder'),
    path('clieingfin/<ning>', views.ClieIngFin, name='clieingfin'),
    path('logout/', views.sesionout, name='sesionout'),
    path('ulist/', login_required(views.UserListView.as_view()), name='ulist'),
    path("udetail/<pk>/", login_required(views.UserDetailView.as_view()), name="udetail"),
    path("ucreate/", views.UserCreateView.as_view(), name="ucreate"),
    path("udelete/<pk>", login_required(views.UserDeleteView.as_view()), name="udelete"),
    path("uupdate/<pk>/", login_required(views.UserUpdateView.as_view()), name="uupdate"),
    path("uprofile/<pk>/", login_required(views.ProfileView.as_view()), name="uprofile"),
    path('tlist/', login_required(views.TramitesListView.as_view()), name='tlist'),
    path("tdetail/<pk>/", login_required(views.TramitesDetailView.as_view()), name="tdetail"),
    path("tcreate/", login_required(views.TramitesCreateView.as_view()), name="tcreate"),
    path("tupdate/<pk>/", login_required(views.TramitesUpdateView.as_view()), name="tupdate"),
    path("tdelete/<pk>", login_required(views.TramitesDeleteView.as_view()), name="tdelete"),
    path('clist/', login_required(views.ClientesListView.as_view()), name='clist'),
    path('cdetail/<pk>', login_required(views.ClientesDetailView.as_view()), name='cdetail'),
    path("ccreate/", login_required(views.ClientesCreateView.as_view()), name="ccreate"),
    path("cupdate/<pk>/", login_required(views.ClientesUpdateView.as_view()), name="cupdate"),
    path("cdelete/<pk>", login_required(views.ClientesDeleteView.as_view()), name="cdelete"),
    path('resetlist/', login_required(views.ContadoresListView.as_view()), name='resetlist'),
    path('resetcount/', views.resetcontadores,name='resetcount'),
    path('recepcion/', login_required(views.IngresosListView.as_view()),name='recepcion'),
    path('recdetail/<ning>/', views.recdetail, name='recdetail'),
    path("reccliente/<ning>/<ndoc>/",views.RecClienteCreateView, name="reccliente"),
    path('anuncios/', login_required(views.AnunciosListView.as_view()),name='anuncios'),
    path('genanun/<rec>/<ning>/<deco>/<cont>/',views.GenerarAnuncio, name='genanun'),
    path('delanun/<nanun>/', views.EliminarAnuncio, name='delanun'),
    path("atender/<ning>/", views.IngresoAtendido, name="atender"),
    path("turnofinal/<ning>/", views.TurnoFinalAtendido, name="turnofinal"),
    path("refreshing/<ning>/", views.IngresoRefresh, name="refreshing"),
    path("confirupclien/<ndoc>/<ning>/",views.ConfirmarCambioDoc, name="confirupclien"),
    path("lugares/", views.Lugares, name="lugares"),
    path("lugaratendido/<ning>/", views.LugarAtendido, name="lugaratendido"),
    path("lugarRefresh/<ning>/", views.LugarRefresh, name="lugarRefresh"),
    path('lugardetail/<ning>/', views.Lugardetail, name='lugardetail'),
    path('lugaranun/<ning>/<deco>/<cont>/<ntram>/',views.LugarGenAnuncio, name='lugaranun'),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
