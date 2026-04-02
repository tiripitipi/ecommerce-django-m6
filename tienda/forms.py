from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    """Formulario de registro que extiende UserCreationForm con campo email."""
    email = forms.EmailField(required=False)

    class Meta(UserCreationForm.Meta):
        User = get_user_model()
        model = User
        # campos que va a mostrar el formulario
        fields = ['username', 'email', 'password1', 'password2']