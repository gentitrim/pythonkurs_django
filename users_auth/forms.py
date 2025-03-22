from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

from .models import CostumUser

class CostumUserRegistrationForm(UserCreationForm):
    class Meta:
        model = CostumUser
        fields = ['username','first_name','last_name','password1','password2']
    

class CostumLoginForm(AuthenticationForm):
    class Meta:
        model = CostumUser
        fields = ['username','password']
