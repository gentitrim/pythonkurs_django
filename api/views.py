from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from .serialisers import MovieReadModelSerializer,MovieCreateModelSerializer,MovieUpdatemodelSerializer
from viewer.models import Movies
from rest_framework.decorators import api_view

# Create your views here.


@api_view(['GET','POST'])

def movies(request):
    if request.method == 'GET':
        pass
        # movies = Movies.objects.all()
        # serializer = MovieSerializer(movies,many=True)
        # return Response(serializer.data)
    elif request.method == 'POST': 
        pass
        # serializer = MovieSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data,status=201)
        # return Response(serializer.errors,status=400)

class MovieListCreate(ListModelMixin,CreateModelMixin,GenericAPIView):
    queryset = Movies.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieReadModelSerializer
        elif self.request.method == 'POST':
            return MovieCreateModelSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)



class MovieDetailDeleteUpdate(RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin,GenericAPIView):
    queryset = Movies.objects.all()
    # lookup_field = 'pk'

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return MovieCreateModelSerializer
        elif self.request.method == 'GET':
            return MovieReadModelSerializer
        else:
            return MovieUpdatemodelSerializer
        
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
       
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    def delete(self,request,*args,**kwargs):    
        return self.destroy(request,*args,**kwargs)
    
    def patch(self,request,*args,**kwargs):
        return self.partial_update(request,*args,**kwargs)