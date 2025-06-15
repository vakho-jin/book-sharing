from rest_framework import serializers
from .models import BookRequest, BookTransfer
from apps.books.models import Book

class BookRequestSerializer(serializers.ModelSerializer):
    book_title = serializers.CharField(source='book.title', read_only=True)
    book_owner = serializers.CharField(source='book.owner.username', read_only=True)
    requester_username = serializers.CharField(source='requester.username', read_only=True)

    class Meta:
        model = BookRequest
        fields = [
            'id', 'book', 'book_title', 'book_owner', 'requester', 
            'requester_username', 'status', 'message', 'owner_response', 
            'created_at', 'updated_at'
        ]
        read_only_fields = ('requester', 'status')

class BookRequestCreateSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.filter(is_available=True)
    )

    class Meta:
        model = BookRequest
        fields = ['book', 'message']

    def validate_book(self, value):
        request = self.context.get('request')
        if request and value.owner == request.user:
            raise serializers.ValidationError("შეუძლებელისა საკუთარი წიგნის მოთხოვნა")
        return value

class BookRequestUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookRequest
        fields = ['status', 'owner_response']

    def validate_status(self, value):
        if value not in ['approved', 'rejected']:
            raise serializers.ValidationError("სტატუსი შესაძლებელია იყოს მხოლოდ ერთი: 'approved' ან 'rejected'")
        return value

class BookTransferSerializer(serializers.ModelSerializer):
    book_title = serializers.CharField(source='book_request.book.title', read_only=True)
    requester_username = serializers.CharField(source='book_request.requester.username', read_only=True)

    class Meta:
        model = BookTransfer
        fields = [
            'id', 'book_request', 'book_title', 'requester_username',
            'transfer_date', 'return_date', 'actual_return_date',
            'owner_rating', 'requester_rating', 'owner_comment', 
            'requester_comment', 'created_at'
        ]