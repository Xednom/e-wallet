from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext as _

from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    models = CustomUser
    readonly_fields = ('created_at', 'updated_at')
    list_display = [
        'username', 'is_active', 'is_staff', 'is_superuser',
        'country', 'state'
        ]
    list_filter = [
        'is_staff', 'is_active', 'is_superuser',
         'country', 'state'
    ]
    UserAdmin.fieldsets = (
        ('User Info', {
            'fields': (
                'username',
                'first_name',
                'last_name',
                'email',
                'address',
                'country',
                'state',
                'zip_code',
            )
        }),
        ('Permissions', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            )
        }),
        ('Important dates', {
            'fields': (
                'last_login',
                'date_joined',
                'created_at',
                'updated_at',
            )
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)
