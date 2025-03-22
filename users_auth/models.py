from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.http import HttpResponse

from django.urls import reverse_lazy

class CostumUser(AbstractUser):
    db_table = "costum_user"

class CostumLogoutView():
    def get(self,request):
        request.session.flush()
        return HttpResponse(reverse_lazy('login'))
