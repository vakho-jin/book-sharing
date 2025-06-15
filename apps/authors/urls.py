from django.urls import path
from . import views

urlpatterns = [
    path('', views.AuthorListCreateView.as_view(), name='author-list-create'),
    path('<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),
]