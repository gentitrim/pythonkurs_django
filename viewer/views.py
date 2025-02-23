from django.shortcuts import render
from django.http import HttpResponse
from .models import Genere
from .models import Movies,Genere


# Create your views here.


def index(request):
    movies = Movies.objects.all()
    return render(request,'index.html',context={"adjectives": {"movie.title","Hi"},"all_movies":movies})

def hello(request,something):
    return HttpResponse(f'hello {something}')

def search(request):
    search_param = request.GET.get("search_param")
    print(request.GET)
    return HttpResponse(f"Searched for {search_param}")

def get_generes(request):
    generes = Genere.objects.all()
    print(generes)
    return HttpResponse(generes)