from django.urls import path
from .views import index, sobre, servicos

urlpatterns = [
    path('', index, name='index'),
    path('sobre/', sobre, name='sobre'),
    path('servicos/', servicos, name='servicos'),
]