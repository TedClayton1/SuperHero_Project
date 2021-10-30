from django.shortcuts import render
from django.http import HttpResponse
from .models import Superhero

# Create your views here.
def index(request):
    all_heroes = Superhero.objects.all()
    context = {
        'all_heroes': all_heroes
    }
    return render(request, 'superheroes/index.html', context)

def detail(request, hero_id):
    single_hero = Superhero.objects.get(pk=hero_id)
    context = {
        'single_hero': single_hero
    }
    return render(request, 'superheroes/detail.html', context )

    def create(request):
        if request.method == "POST":
            # save the form contents as a new db object
            # return to index
            name = request.POST.get('name')
            alter_ego = request.POST.get('alter_ego')
            primary = request.POST.get('primary')
            secondary = request.POST.get('secondary')
            catchphrase = request.POST.get('catchphrase')
        else:
            return render(request, 'superheroes/create.html')