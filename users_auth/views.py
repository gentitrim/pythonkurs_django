from django.shortcuts import render
from django.views.generic import CreateView,FormView
from .models import CostumUser
from django.urls import reverse_lazy
from .forms import CostumUserRegistrationForm,CostumLoginForm
from django.contrib.auth.views import LoginView,LogoutView
from django.http import HttpResponseRedirect

# Create your views here.
class CostumRegistrationView(CreateView):
    template_name = "user_registration.html"
    model = CostumUser
    form_class = CostumUserRegistrationForm
    success_url = reverse_lazy("login")


class CostumLoginView(LoginView):
    model = CostumUser
    template_name = "user_login.html"
    form_class = CostumLoginForm
    success_url = reverse_lazy("index")

class CostumLogoutView(LogoutView):
    def get(self,request):
        form = CostumLogoutView()
        return render(request,'confirm_logout.html',{'form':form})
    def post(self, request):
        return HttpResponseRedirect(reverse_lazy('login'))
    
    
    