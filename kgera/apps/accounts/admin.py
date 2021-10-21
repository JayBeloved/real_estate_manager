from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()


class UserAdmin(UserAdmin):
    pass


# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(Profile)
