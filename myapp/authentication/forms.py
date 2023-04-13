from django import forms
from django.contrib.auth.forms import UserCreationForm
from myapp.models import CustomUser

class SignUpForm(UserCreationForm):
    # ... (code for SignUpForm)
    is_organizer = forms.BooleanField(required=False, initial=False, label='Organisateur')

    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'is_organizer')