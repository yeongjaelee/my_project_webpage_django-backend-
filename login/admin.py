from django.contrib import admin

from login.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
