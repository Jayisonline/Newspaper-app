from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


# Register your models here.


from .forms import CustomUserCreationForm, UserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'age', 'is_staff', ] # new



admin.site.register(CustomUser ,CustomUserAdmin)