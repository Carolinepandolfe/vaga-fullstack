from django.urls import path
from .views import list_pokemons

urlpatterns = [
    path('', list_pokemons, name='list_pokemons')
]