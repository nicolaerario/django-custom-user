from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    # list_display = ['email', 'username', 'is_staff', 'custom_field', ] to control the fiels listed on admin b.e.


admin.site.register(CustomUser, CustomUserAdmin)
