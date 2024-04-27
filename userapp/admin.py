from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# class CustomUserAdmin(UserAdmin):
    # Define the fields to be displayed in the admin panel
    # fieldsets = (
    #     (None, {'fields': ('phone_number', 'password')}),
    #     ('Personal info', {'fields': ('username', 'last_name', 'picture', 'role')}),
    #     ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    #     ('Important dates', {'fields': ('last_login', 'date_joined')}),
    # )
    # # Define the fields to be displayed in the user list
    # list_display = ('username', 'last_name', 'phone_number', 'role', 'is_staff')
    # # Define the field to be used for searching users
    # search_fields = ('username', 'last_name', 'phone_number')
    # # Define the fields to be used for filtering users
    # list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    #
    # # Override the save_model method to ensure username is set
    # def save_model(self, request, obj, form, change):
    #     if not obj.username:
    #         obj.username = obj.phone_number
    #     super().save_model(request, obj, form, change)

# Register the custom UserAdmin
admin.site.register(User)
