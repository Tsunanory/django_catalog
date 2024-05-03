from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.translation import gettext_lazy as _

from catalog.forms import FormStyleMixin
from users.models import User


class UserRegisterForm(FormStyleMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')
    password1 = forms.CharField(
        label=_("Пароль"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Подтверждение пароля"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=_("Повторно введите выбранный пароль"),
    )
    # R45678uyt
    # username = forms.CharField(label=_("Почта"))
    # password = forms.CharField(label=_("Пароль"), widget=forms.PasswordInput)


# class CustomUserCreationForm(UserCreationForm):
#     email = forms.EmailField(label=_('почта'), required=True)
#     class Meta:
#         models = User
#         field

    # password = forms.CharField(label=_("Пароль"), widget=forms.PasswordInput)
    # confirm_password = forms.CharField(label=_("Подтверждение пароля"), widget=forms.PasswordInput)
