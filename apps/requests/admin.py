from django.contrib import admin
from .models import BookRequest, BookTransfer

@admin.register(BookRequest)
class BookRequestAdmin(admin.ModelAdmin):
    list_display = ('book', 'requester', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('book__title', 'requester__username')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(BookTransfer)
class BookTransferAdmin(admin.ModelAdmin):
    list_display = ('book_request', 'transfer_date', 'return_date', 'owner_rating', 'requester_rating')
    list_filter = ('transfer_date', 'return_date')
    readonly_fields = ('created_at',)