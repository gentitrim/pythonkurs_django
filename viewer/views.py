from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Genere,Director
from .models import Movies
from django.views import View
from django.views.generic import TemplateView,ListView,FormView,UpdateView,DeleteView
from .forms import MovieForm,DirectorForm,MovieModelForm
from django.urls import reverse_lazy
from logging import getLogger
from django.contrib.auth.mixins import PermissionRequiredMixin,LoginRequiredMixin

# Create your views here.

LOGGER = getLogger()

#Function based views
def movies(request):
    movies = Movies.objects.all()
    return render(request,'movies.html',context={"all_movies":movies})

def index(request):
    return render(request,'index.html')


#class based view
class MoviesView(View):
    def get(self,request):
        movies = Movies.objects.all()
        return render(request,'movies.html',context={"all_movies":movies})
    
    def post(self,request):
        pass
    
#Class template based view njelloj si class based view
class MoviesTemplateView(TemplateView):
    template_name = 'movies.html'
    extra_context = {"all_movies":Movies.objects.all()}


#class based listview

class MoviesListView(ListView):
    template_name = 'movies.html'
    model = Movies
    context_object_name = "all_movies"


#Form view
class MovieCreateFormView(LoginRequiredMixin,PermissionRequiredMixin,FormView):
    
    template_name ='createmovie.html'
    form_class = MovieForm
    success_url = reverse_lazy('movies')
    permission_required = ["viewer.add_movies"]
    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        Movies.objects.create(
            title=cleaned_data["title"],
            rated = cleaned_data["rated"],
            released = cleaned_data["released"],
            description = cleaned_data["description"],
            genere = cleaned_data["genere"]

        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        LOGGER.error("Form is not valid")
        return super().form_invalid(form)
    

class DirectorCreateFormView(FormView):
    template_name = "create_director.html"
    form_class = DirectorForm
    success_url = reverse_lazy('directors')
    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        Director.objects.create(
            name=cleaned_data["name"],
            surname = cleaned_data["surname"],
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        LOGGER.error("Form is not valid")
        return super().form_invalid(form)

class DirectorListView(ListView):
    template_name = 'directors.html'
    model = Director
    context_object_name = "all_directors"


class MovieUpdateView(UpdateView):
    form_class = MovieModelForm
    template_name = "createmovie.html"
    model = Movies
    success_url = reverse_lazy("movies")
    

class MoviesSimpleUpdateView(View):
    def get(self,request,pk):
        movie = Movies.objects.get(id = pk)
        prefilled_form  = MovieModelForm(instance=movie)
        return render(request,"createmovie.html",context={"form":prefilled_form})
    
    def post(self,request,pk):
        movie = Movies.objects.get(id = pk)
        new_filled_form = MovieModelForm(request.POST,instance = movie)
        if new_filled_form.is_valid():
            new_filled_form.save()
            return HttpResponseRedirect(reverse_lazy("movies")) 
        

class MovieDeleteView(DeleteView):
    template_name = 'confirmdelete.html'
    model = Movies
    success_url = reverse_lazy("movies")


class SimpleDeleteView(View):
    def get(self,request,pk):
        movie = Movies.objects.get(id = pk)
        return render(request,"confitmdelete.html",context={"object":movie})
    def post(self,request,pk):
        movie = Movies.objects.get(id = pk)
        movie.delete()
        return HttpResponseRedirect(reverse_lazy("movies"))