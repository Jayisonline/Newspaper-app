from pyexpat import model
from django import forms


from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser
# import django.utils.lru_cache



class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('age', )



class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields


