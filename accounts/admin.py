from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ("email", "username", "role", "is_active", "date_joined")
    list_filter = ("role", "is_active")
    search_fields = ("email", "username", "mobile_number")
    fieldsets = UserAdmin.fieldsets + (
        ("Extra info", {"fields": ("mobile_number", "profile_image", "role")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Extra info", {"fields": ("email", "mobile_number", "role")}),
    )