from rest_framework import serializers
from .models import Author

class AuthorSerializer(serializers.ModelSerializer):
    books_count = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = '__all__'

    def get_books_count(self, obj):
        return obj.books.count()

class AuthorDetailSerializer(serializers.ModelSerializer):
    books = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Author
        fields = '__all__'