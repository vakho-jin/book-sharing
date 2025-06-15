from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookRequestListCreateView.as_view(), name='request-list-create'),
    path('incoming/', views.incoming_requests, name='incoming-requests'),
    path('<int:pk>/handle/', views.handle_request, name='handle-request'),
    path('<int:request_id>/transfer/', views.create_transfer, name='create-transfer'),
    path('transfers/', views.my_transfers, name='my-transfers'),
]