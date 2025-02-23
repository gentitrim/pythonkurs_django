from django.urls import path

from . import views


urlpatterns = [
    path('',views.index),
    path('index/<something>',views.hello),
    path('index/search/',views.search),
    path('generes/',views.get_generes),
]
