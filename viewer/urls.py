from django.urls import path

from . import views


urlpatterns = [
    path('',views.index,name="index"),
    # path('movies/',views.movies,name="movies"), #function based urls
    #path('movies/',views.MoviesTemplateView.as_view(),name="movies")
    # path('movies/',views.MoviesTemplateView.as_view(),name="movies") #Class templateview based urls
    path('movies/',views.MoviesListView.as_view(),name="movies"), #Class listview based urls,
    # path('movies/create',views.MovieCreateFormView.as_view(),name="create_movies")
    path('movies/create',views.MovieCreateFormView.as_view(),name="create_movies"),
    path('director/create',views.DirectorCreateFormView.as_view(),name="create_director"),
    path('director/',views.DirectorListView.as_view(),name="directors")
]
