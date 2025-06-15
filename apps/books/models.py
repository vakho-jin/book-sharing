from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class BookCondition(models.Model):
    CONDITION_CHOICES = [
        ('excellent', 'საუკეთესო'),
        ('good', 'კარგი'),
        ('fair', 'დამაკმაყოფილებელი'),
        ('poor', 'დაზიანებული'),
    ]
    
    name = models.CharField(max_length=20, choices=CONDITION_CHOICES, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.get_name_display()

class Book(models.Model):
    title = models.CharField(max_length=300)
    authors = models.ManyToManyField('authors.Author', related_name='books')
    genres = models.ManyToManyField(Genre, related_name='books')
    isbn = models.CharField(max_length=13, blank=True)
    publication_year = models.IntegerField()
    publisher = models.CharField(max_length=200, blank=True)
    pages = models.IntegerField(blank=True, null=True)
    language = models.CharField(max_length=50, default='Русский')
    description = models.TextField(blank=True)
    cover_image = models.ImageField(upload_to='books/covers/', blank=True)
    
    # მფლობელის და მდგომარეობის შესახებ
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_books')
    condition = models.ForeignKey(BookCondition, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)
    pickup_location = models.CharField(max_length=300)
    pickup_instructions = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} ({self.publication_year})"