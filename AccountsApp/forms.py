from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    name = forms.CharField()
    description = forms.CharField()
    web = forms.URLField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'name', 'description', 'web', 'email',
                  'password1', 'password2', ]
        help_texts = {k: "" for k in fields}


class UserEditForm(UserCreationForm):
    #username = forms.CharField(label='Modificar nombre de usuario')
    email = forms.EmailField(label="Modificar email")
    web = forms.URLField(label="Modificar url")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)
    name = forms.CharField(max_length=50, label="Modificar nombre")
    description = forms.CharField(max_length=500, label="Modificar descripción")

    class Meta:
        model = User
        fields = ['email','password1', 'password2', 'name', 'description', 'web']
        help_texts = {k: "" for k in fields}

class AvatarForm(forms.Form):
    avatar = forms.ImageField(required=True)
