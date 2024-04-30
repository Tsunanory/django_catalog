from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.views.generic import CreateView

# from users.forms import CustomUserCreationForm
from users.models import User


class RegisterView(CreateView):
    model = User
    # form_class = CustomUserCreationForm
    template_name = 'users/register.html'
