from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django.forms import ModelForm

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "password1", "password2"]



class MyuserChangeForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "bio", "birth_of_date"]

