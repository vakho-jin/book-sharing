from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookListCreateView.as_view(), name='book-list-create'),
    path('<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('my-books/', views.my_books, name='my-books'),
    path('genres/', views.GenreListCreateView.as_view(), name='genre-list'),
    path('conditions/', views.BookConditionListView.as_view(), name='condition-list'),
]