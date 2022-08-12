from django.urls import path
from . import views


urlpatterns = [
    path('caller/', views.caller, name='caller'),
    path('anunws/', views.callerws.as_view()),
]
