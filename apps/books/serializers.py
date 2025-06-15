from rest_framework import serializers
from .models import Book, Genre, BookCondition
from apps.authors.serializers import AuthorSerializer
from apps.authors.models import Author

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class BookConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCondition
        fields = '__all__'

class BookListSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)
    condition = BookConditionSerializer(read_only=True)
    owner_username = serializers.CharField(source='owner.username', read_only=True)

    class Meta:
        model = Book
        fields = [
            'id', 'title', 'authors', 'genres', 'publication_year', 
            'cover_image', 'condition', 'is_available', 'pickup_location',
            'owner_username', 'created_at'
        ]

class BookDetailSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)
    condition = BookConditionSerializer(read_only=True)
    owner_username = serializers.CharField(source='owner.username', read_only=True)
    requests_count = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = '__all__'
        read_only_fields = ('owner',)

    def get_requests_count(self, obj):
        return obj.requests.filter(status='pending').count()

class BookCreateUpdateSerializer(serializers.ModelSerializer):
    authors = serializers.PrimaryKeyRelatedField(
        many=True, 
        queryset=Author.objects.all()
    )
    genres = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Genre.objects.all()
    )
    condition = serializers.PrimaryKeyRelatedField(
        queryset=BookCondition.objects.all()
    )

    class Meta:
        model = Book
        exclude = ['owner']

    def to_representation(self, instance):
        return BookDetailSerializer(instance, context=self.context).data