from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User as UserModel
from .forms import SignUpChangeForm, SignUpForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.admin import GroupAdmin, UserAdmin


class CustomAdmin(UserAdmin):
    add_form = SignUpForm
    form = SignUpChangeForm
    readonly_fields = ['user_id']

    fieldsets = (
        (None, {'fields': ('email', 'password', 'user_id')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)


admin.site.register(UserModel, CustomAdmin)
admin.site.register(Permission)



