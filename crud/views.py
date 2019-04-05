from django.shortcuts import render
from .models import Pokemon

# Create your views here.

def list_pokemons(request):
    pokemons = Pokemon.objects.all()
    return render(request, 'pokemons.html', {'pokemons': pokemons})