from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class BookRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'ლოდინის რეჟიმი'),
        ('approved', 'დადასტურებულია'),
        ('rejected', 'უარყოფილია'),
        ('completed', 'დასრულებულია'),
        ('cancelled', 'უარყოფილია'),
    ]
    
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE, related_name='requests')
    requester = models.ForeignKey(User, on_delete=models.CASCADE, related_name='book_requests')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    message = models.TextField(blank=True, help_text="მომთხოვნის შეტყობინება")
    owner_response = models.TextField(blank=True, help_text="მფლობელის პასუხი")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ['book', 'requester']
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.requester.username} ითხოვს {self.book.title}"

class BookTransfer(models.Model):
    book_request = models.OneToOneField(BookRequest, on_delete=models.CASCADE)
    transfer_date = models.DateTimeField()
    return_date = models.DateTimeField(blank=True, null=True)
    actual_return_date = models.DateTimeField(blank=True, null=True)
    
    # Рейтинги после завершения обмена
    owner_rating = models.IntegerField(blank=True, null=True, help_text="რეიტინგი 1-დან 5-მდე")
    requester_rating = models.IntegerField(blank=True, null=True, help_text="რეიტინგი 1-დან 5-მდე")
    owner_comment = models.TextField(blank=True)
    requester_comment = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"გადაცემა: {self.book_request.book.title}"