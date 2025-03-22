from django.urls import path

from . import views


urlpatterns = [
    path('auth/register',views.CostumRegistrationView.as_view(),name="register"),
    path('',views.CostumLoginView.as_view(),name="login"),
    path('auth/logout',views.CostumLogoutView.as_view(),name="logout"),
]