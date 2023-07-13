from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#firstname = models.CharField(max_length=50)
#surname   = models.CharField(max_length=50)
#email     = models.EmailField()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
