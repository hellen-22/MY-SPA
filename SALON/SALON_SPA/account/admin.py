from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import *
from .models import *

# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ('first_name', 'last_name', 'username', 'email', 'password')
    search_fields = ('first_name', 'username')
    readonly_fields = ('date_joined', 'last_login')
    filter_horizontal = ()
    list_filter = ('last_login',)
    fieldsets = ()
    ordering = ('first_name',)
    add_form = CustomUserForm
    change_form = PasswordChangingForm
    form = AccountEditForm
    model = CustomUser
    add_fieldsets = ((None, {'fields': 
    ('username', 'password', 'confirm_password')}),
    ('Personal info', {'fields': ('first_name','last_name', 'email','date_joined')}),
    ('Permissions', {'fields': ('is_active','is_staff')}),)



admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Appointment)