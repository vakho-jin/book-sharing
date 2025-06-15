from django.contrib import admin
from .models import Author

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date', 'death_date', 'created_at')
    search_fields = ('name', 'biography')
    list_filter = ('birth_date', 'death_date', 'created_at')
    readonly_fields = ('created_at',)