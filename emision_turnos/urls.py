from django.urls import path
from . import views

urlpatterns = [
    path('touch/', views.touch, name='touch'),
    path('touch/confirm/<ndoc>/<ntram>', views.confirm, name='confirm'),
]
