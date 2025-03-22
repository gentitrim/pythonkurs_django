from django.urls import path
from .views import MovieListCreate,MovieDetailDeleteUpdate


urlpatterns = [
    path('/movies',MovieListCreate.as_view(),name='api-movies'),
    path('/movies/<pk>',MovieDetailDeleteUpdate.as_view(),name='api-movie'),
]
