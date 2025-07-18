from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def clean_email(self):
        new_email = self.cleaned_data.get('email')
        if User.objects.filter(email = new_email).exists():
            raise ValidationError("This Email Is Already Taken!")
        return new_email
