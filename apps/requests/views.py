from rest_framework import generics, status, serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import BookRequest, BookTransfer
from .serializers import (
    BookRequestSerializer, BookRequestCreateSerializer, 
    BookRequestUpdateSerializer, BookTransferSerializer
)
from apps.books.models import Book

class BookRequestListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return BookRequest.objects.filter(requester=self.request.user).select_related('book', 'book__owner')
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BookRequestCreateSerializer
        return BookRequestSerializer
    
    def perform_create(self, serializer):
        book = serializer.validated_data['book']
        if book.owner == self.request.user:
            raise serializers.ValidationError({"book": "შეუძლებელია საკუთარი წიგნის მოთხოვნა"})
        if not book.is_available:
            raise serializers.ValidationError({"book": "წიგნი მიუწვდომელია"})
        
        # Проверяем, не существует ли уже запрос от этого пользователя на эту книгу
        if BookRequest.objects.filter(book=book, requester=self.request.user).exists():
            raise serializers.ValidationError({"book": "მოთხოვნა უკვე გაგზავნილია"})
            
        serializer.save(requester=self.request.user)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def incoming_requests(request):
    requests = BookRequest.objects.filter(
        book__owner=request.user,
        status='pending'
    ).select_related('book', 'requester')
    
    serializer = BookRequestSerializer(requests, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def handle_request(request, pk):
    book_request = get_object_or_404(
        BookRequest, 
        pk=pk, 
        book__owner=request.user,
        status='pending'
    )
    
    serializer = BookRequestUpdateSerializer(book_request, data=request.data, partial=True)
    if serializer.is_valid():
        updated_request = serializer.save()
        
        if updated_request.status == 'approved':
            BookRequest.objects.filter(
                book=updated_request.book,
                status='pending'
            ).exclude(pk=updated_request.pk).update(status='rejected')
            
            # Помечаем книгу как недоступную
            updated_request.book.is_available = False
            updated_request.book.save()
        
        return Response(BookRequestSerializer(updated_request).data)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_transfer(request, request_id):
    book_request = get_object_or_404(
        BookRequest,
        pk=request_id,
        book__owner=request.user,
        status='approved'
    )
    
    serializer = BookTransferSerializer(data=request.data)
    if serializer.is_valid():
        transfer = serializer.save(book_request=book_request)
        book_request.status = 'completed'
        book_request.save()
        return Response(BookTransferSerializer(transfer).data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_transfers(request):
    transfers = BookTransfer.objects.filter(
        book_request__requester=request.user
    ).select_related('book_request__book')
    
    serializer = BookTransferSerializer(transfers, many=True)
    return Response(serializer.data)