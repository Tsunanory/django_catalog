from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.translation import gettext_lazy as _

from catalog.forms import FormStyleMixin
from users.models import User


class UserRegisterForm(FormStyleMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')
    username = forms.CharField(label=_("Почта"))
    password = forms.CharField(label=_("Пароль"), widget=forms.PasswordInput)


# class CustomUserCreationForm(UserCreationForm):
#     email = forms.EmailField(label=_('почта'), required=True)
#     class Meta:
#         models = User
#         field

    # password = forms.CharField(label=_("Пароль"), widget=forms.PasswordInput)
    # confirm_password = forms.CharField(label=_("Подтверждение пароля"), widget=forms.PasswordInput)
