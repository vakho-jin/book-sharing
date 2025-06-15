from django.contrib import admin
from .models import Book, Genre, BookCondition

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(BookCondition)
class BookConditionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_year', 'owner', 'condition', 'is_available', 'created_at')
    list_filter = ('genres', 'condition', 'is_available', 'publication_year', 'created_at')
    search_fields = ('title', 'authors__name', 'owner__username')
    filter_horizontal = ('authors', 'genres')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('ძირითადი ინფორმაცია', {
            'fields': ('title', 'authors', 'genres', 'isbn', 'publication_year', 'publisher', 'pages', 'language')
        }),
        ('აღწერა', {
            'fields': ('description', 'cover_image')
        }),
        ('მფლობელი და მდგომარეობა', {
            'fields': ('owner', 'condition', 'is_available', 'pickup_location', 'pickup_instructions')
        }),
        ('თარიღები', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )