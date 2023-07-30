from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from core.models import User

# Register your models here.

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    search_fields = ('username','first_name', 'last_name', 'email')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    list_display = ('username', 'email', 'first_name', 'last_name')
    exclude = ['password']
    readonly_fields = ('last_login', 'date_joined')

admin.site.unregister(Group)