from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser, CustomerProfile

class CustomUserAdmin(BaseUserAdmin):
    # The fields to be used in displaying the User model.
    list_display = ('email', 'phone_no', 'is_staff', 'is_active', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    
    # Fieldsets for editing users
    fieldsets = (
        (None, {'fields': ('email', 'phone_no', 'password')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login',)}),
    )

    # Fieldsets for creating a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'phone_no', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser')}
        ),
    )

    search_fields = ('email', 'phone_no')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions')

# Register the CustomUser and CustomerProfile in the admin
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(CustomerProfile)
