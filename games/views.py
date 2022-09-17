from django.shortcuts import render
from django.views.generic import ListView,DetailView
from games.models import Game
class GameListView(ListView):
    model = Game
    template_name = 'game/home.html'
    context_object_name = 'game_list'
def home(request):
    return render(request, 'home.html')
class GameDetailView(DetailView):
    model = Game
    context_object_name = 'game'    
# Create your views here.
