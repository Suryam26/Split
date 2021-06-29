from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Bill, Item, Consumer


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm


admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Bill)
admin.site.register(Item)
admin.site.register(Consumer)
