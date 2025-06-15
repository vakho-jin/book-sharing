from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'is_staff', 'is_active', 'date_joined', 'rating')
    list_filter = ('is_staff', 'is_active', 'date_joined')
    fieldsets = UserAdmin.fieldsets + (
        ('დამატებითI ინფორმაცია', {'fields': ('phone', 'location', 'bio', 'rating')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('დამატებითI ინფორმაცია', {'fields': ('email', 'phone', 'location', 'bio')}),
    )
    search_fields = ('email', 'username')
    ordering = ('email',)