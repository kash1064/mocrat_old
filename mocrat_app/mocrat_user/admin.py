from .models import User, ChibaMokuUser
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.utils.translation import gettext, gettext_lazy as _

@admin.register(User)
class AdminUserAdmin(UserAdmin):

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {
         'fields': ('email', )}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'email', 'is_staff')
    search_fields = ('username', 'email')
    filter_horizontal = ('groups', 'user_permissions')

class ChibaMokuUserAdmin(admin.ModelAdmin):
    fields = ['discord_id', 'display_name', 'level', 'total_exp', 'created_at', 'updated_at']

admin.site.register(ChibaMokuUser, ChibaMokuUserAdmin)